from django.shortcuts import render, redirect
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if util.get_entry(title) is None:
        return render(request, "encyclopedia/error.html", {
            "message": "This entry does not exist."
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": util.get_entry(title)
        })
    
def search(request):
    query = request.GET.get("q")
    entries = util.list_entries()
    print(f"Search query: {query}")
    print(f"Available entries: {entries}")
    
    # Primera verificación: coincidencia exacta case-insensitive
    for entry in entries:
        if query.lower() == entry.lower():
            print(f"Exact match found: {entry}")
            return redirect(f"/wiki/{entry}")
    
    matches = []
    for entry in entries:
        if query.lower() in entry.lower():
            print(f"Partial match found: {entry}")
            matches.append(entry)

    print(f"Total matches found: {len(matches)}")
    print(f"Matches list: {matches}")

    if len(matches) == 1:
        print(f"Single match - redirecting to: {matches[0]}")
        return redirect(f"/wiki/{matches[0]}")
    else:
        print(f"Multiple or zero matches - rendering search page")
        return render(request, "encyclopedia/search.html", {
            "query": query,
            "entries": matches
        })



