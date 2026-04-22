from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Project, Skill, Education, Experience, Interest, ContactMessage


def home(request):
    featured_projects = Project.objects.filter(featured=True)[:3]
    skills = Skill.objects.all()
    context = {
        'featured_projects': featured_projects,
        'skills': skills,
    }
    return render(request, 'main/home.html', context)


def about(request):
    education = Education.objects.all()
    experience = Experience.objects.all()
    interests = Interest.objects.all()
    context = {
        'education': education,
        'experience': experience,
        'interests': interests,
    }
    return render(request, 'main/about.html', context)


def projects(request):
    all_projects = Project.objects.all()
    status_filter = request.GET.get('status', '')
    if status_filter:
        all_projects = all_projects.filter(status=status_filter)
    context = {
        'projects': all_projects,
        'status_filter': status_filter,
    }
    return render(request, 'main/projects.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    related = Project.objects.exclude(pk=project.pk)[:3]
    context = {
        'project': project,
        'related': related,
    }
    return render(request, 'main/project_detail.html', context)


def skills(request):
    technical = Skill.objects.filter(category='technical')
    tools = Skill.objects.filter(category='tools')
    soft = Skill.objects.filter(category='soft')
    languages = Skill.objects.filter(category='language')
    context = {
        'technical': technical,
        'tools': tools,
        'soft': soft,
        'languages': languages,
    }
    return render(request, 'main/skills.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_text = request.POST.get('message', '').strip()

        if name and email and subject and message_text:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text,
            )
            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'main/contact.html')
