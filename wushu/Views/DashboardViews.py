from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# from rest_framework_simplejwt import views as jwt_views
from django.http import JsonResponse

from wushu.models import SportClubUser, SportsClub, Coach, Level, License, Athlete, Person, Judge
from wushu.services import general_methods
from wushu.models.EnumFields import EnumFields

from wushu.models.CategoryItem import CategoryItem
# from rest_framework.authtoken.models import Token


from datetime import date,datetime


@login_required
def return_athlete_dashboard(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    return render(request, 'anasayfa/sporcu.html')


@login_required
def return_referee_dashboard(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    return render(request, 'anasayfa/hakem.html')


@login_required
def return_coach_dashboard(request):
    perm = general_methods.control_access(request)
    #
    # if not perm:
    #     logout(request)
    #
    #     return redirect('accounts:login')
    return render(request, 'anasayfa/antrenor.html')


@login_required
def return_directory_dashboard(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    return render(request, 'anasayfa/federasyon.html')


@login_required
def return_club_user_dashboard(request):
    perm = general_methods.control_access(request)
    # x = general_methods.import_csv()

    if not perm:
        logout(request)
        return redirect('accounts:login')

    clubuser = SportClubUser.objects.get(user=request.user)
    clubs = SportsClub.objects.filter(clubUser=clubuser)
    clubsPk = []
    for club in clubs:
        clubsPk.append(club.pk)

    total_club_user = club.clubUser.count()
    total_coach = Coach.objects.filter(sportsclub=club).count()
    total_athlete = Athlete.objects.filter(licenses__sportsClub__in=clubsPk).distinct().count()

    athletes = Athlete.objects.filter(licenses__sportsClub__in=clubsPk, belts__startDate__year=2020,
                                      belts__dekont='').distinct()
    print(EnumFields.WUSHU.value)
    wushu = CategoryItem.objects.filter(forWhichClazz="BELT", branch=EnumFields.WUSHU.value).order_by('-creationDate')
    aikido = CategoryItem.objects.filter(forWhichClazz="BELT").filter(branch=EnumFields.AIKIDO.value).order_by(
        '-creationDate')
    wingChun = CategoryItem.objects.filter(forWhichClazz="BELT").filter(branch=EnumFields.WINGCHUN.value).order_by(
        '-creationDate')
    kyokushin = CategoryItem.objects.filter(forWhichClazz="BELT").filter(branch=EnumFields.KYOKUSHIN.value).order_by(
        '-creationDate')
    jetKuneDo = CategoryItem.objects.filter(forWhichClazz="BELT").filter(branch=EnumFields.JEETKUNEDO.value).order_by(
        '-creationDate')
    return render(request, 'anasayfa/kulup-uyesi.html',
                  {'total_club_user': total_club_user,
                   'total_coach': total_coach,
                   'athletes': athletes,
                   'total_athlete': total_athlete,
                   'wushu': wushu,
                   'aikido': aikido,
                   'wingChun': wingChun,
                   'kyokushin': kyokushin,
                   'jetKuneDo': jetKuneDo,

                   })


@login_required
def return_admin_dashboard(request):
    perm = general_methods.control_access(request)
    # x = general_methods.import_csv()

    if not perm:
        logout(request)
        return redirect('accounts:login')

    if not perm:
        logout(request)
        return redirect('accounts:login')
    # son eklenen 8 sporcuyu ekledik
    last_athlete=Athlete.objects.order_by('-creationDate')[:8]
    total_club = SportsClub.objects.all().count()
    total_athlete = Athlete.objects.all().count()
    total_athlete_gender_man=Athlete.objects.filter(person__gender='Erkek').count()
    total_athlete_gender_woman= Athlete.objects.filter(person__gender='Kadın').count()
    total_athlate_last_month=Athlete.objects.exclude(user__date_joined__month=datetime.now().month).count()
    total_club_user = SportClubUser.objects.all().count()
    total_coachs = Coach.objects.all().count()
    total_brans_aikido=Athlete.objects.filter(licenses__branch='AIKIDO').count()
    total_brans_wushu=Athlete.objects.filter(licenses__branch='WUSHU').count()
    total_brans_wing_chun=Athlete.objects.filter(licenses__branch='WING CHUN').count()
    total_brans_kyokushin_ashihara=Athlete.objects.filter(licenses__branch='KYOKUSHIN ASHIHARA').count()
    total_brans_jeet_kune_do_kulelkavi=Athlete.objects.filter(licenses__branch='JEET KUNE DO KULELKAVIDO').count()
    return render(request, 'anasayfa/admin.html',
                  {'total_club_user': total_club_user, 'total_club': total_club,
                   'total_athlete': total_athlete, 'total_coachs':total_coachs,'last_athletes':last_athlete,'total_athlete_gender_man':total_athlete_gender_man,
                   'total_athlete_gender_woman':total_athlete_gender_woman,'total_athlate_last_month':total_athlate_last_month,
                   'total_brans_wushu':total_brans_wushu,'total_brans_aikido':total_brans_aikido,'total_brans_wing_chun':total_brans_wing_chun,
                   'total_brans_kyokushin_ashihara':total_brans_kyokushin_ashihara,'total_brans_jeet_kune_do_kulelkavi':total_brans_jeet_kune_do_kulelkavi
                   })

@login_required
def City_athlete_cout(request):

    if request.method == 'POST' and request.is_ajax():
        try:
            athletecout = Athlete.objects.filter(communication__city__name__icontains=request.POST.get('city')).count()
            coachcout = Coach.objects.filter(communication__city__name__icontains=request.POST.get('city')).count()
            refereecout = Judge.objects.filter(communication__city__name__icontains=request.POST.get('city')).count()
            sportsClub = SportsClub.objects.filter(
                communication__city__name__icontains=request.POST.get('city')).count()
            data = {
                'athlete': athletecout,
                'coach': coachcout,
                'referee': refereecout,
                'sportsClub': sportsClub

            }
            return JsonResponse(data)
        except Level.DoesNotExist:
            return JsonResponse({'status':'Fail'})

    else:
        return JsonResponse({'status': 'Fail'})
#
#
