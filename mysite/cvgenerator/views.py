from django.shortcuts import render, redirect
from .models import Profile
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa 
from django.template import loader

# import pdfkit
# from django.http import HttpResponse
# from django.template import loader
# import io


def accept(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summary = request.POST.get("summary", "")
        degree = request.POST.get("degree", "")
        school = request.POST.get("school", "")
        university = request.POST.get("university", "")
        experience = request.POST.get("experience", "")
        skills = request.POST.get("skills", "")

        profile = Profile(
            name=name,
            email=email,
            phone=phone,
            summary=summary,
            degree=degree,
            school=school,
            university=university,
            experience= experience,
            skills=skills,
        )
        profile.save()

        # # Redirect to a success page or any other page you desire
        # return redirect('cvgenerator/success_page.html')

    return render(request, 'cvgenerator/accept.html')


def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('cvgenerator/resume.html')

    html = template.render({'user_profile':user_profile})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="my_report.pdf"'

    result = pisa.CreatePDF(html, dest=response)
    if result.err:
        return HttpResponse('problem '+html+'ok')
    return response



def list(request):
    profiles = Profile.objects.all()
    return render(request, 'cvgenerator/list.html',{'profiles':profiles})