from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Group
from .forms import GroupForm

@login_required
def manage_groups(request, group_id=None):
    if group_id:
        group = get_object_or_404(Group, id=group_id)
    else:
        group = None

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('manage_groups')  # Redirige a la misma vista después de crear o actualizar el grupo
    else:
        form = GroupForm(instance=group)  # Esta línea debería estar en la sección `else`

    groups = Group.objects.all()
    
    return render(request, 'manage/admin_manage_groups.html', {'form': form, 'groups': groups, 'group': group})
