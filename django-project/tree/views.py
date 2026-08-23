from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tree, Fruit

@login_required
def tree_view(request, page=1):
    if not Tree.objects.exists():
        Tree.objects.create(page_number=1)

    total_trees = Tree.objects.count()
    current_tree = Tree.objects.filter(page_number=page).first()
    
    if not current_tree:
        return redirect('tree:tree_view', page=total_trees)

    return render(request, 'tree/tree.html', {
        'tree': current_tree,
        'fruits': current_tree.fruits.all(),
        'current_page': current_tree.page_number,
        'total_pages': total_trees,
    })


@login_required
def fruit_create(request, tree_id):
    tree = get_object_or_404(Tree, pk=tree_id)

    if request.method == "POST":
        content = request.POST.get("content", "").strip()

        if content and len(content) <= 20:
            if tree.is_full:
                new_page = Tree.objects.count() + 1
                tree = Tree.objects.create(page_number=new_page)

            Fruit.objects.create(
                tree=tree,
                author=request.user,
                content=content
            )

    return redirect('tree:tree_view', page=tree.page_number)