import re


def getURLName(l):
    urlpattern = r'(/\w+|/\w+:\w+)+"'
    urls = re.search(urlpattern, l)
    # namepattern = r'>[\w+\s]\w<'
    # names = re.findall(namepattern, l)
    # results =  []
    #urls = [m.group(0) for m in urls]
    print(urls.group(0))
    # print(names)
    # for url, name in zip(urls, names):
    #     results.append(f"{url}, {name}")
    # return results
input = """
<div class="portal" role="navigation" id='p-navigation'>
<h3>Navigation</h3>
<div class="body">
<ul>
 <li id="n-mainpage-description"><a href="/wiki/Main_Page" title="Visit the main page [z]" accesskey="z">Main page</a></li>
 <li id="n-contents"><a href="/wiki/Portal:Contents" title="Guides to browsing Wikipedia">Contents</a></li>
 <li id="n-featuredcontent"><a href="/wiki/Portal:Featured_content" title="Featured content  the best of Wikipedia">Featured content</a></li>
<li id="n-currentevents"><a href="/wiki/Portal:Current_events" title="Find background information on current events">Current events</a></li>
<li id="n-randompage"><a href="/wiki/Special:Random" title="Load a random article [x]" accesskey="x">Random article</a></li>
<li id="n-sitesupport"><a href="//donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en" title="Support us">Donate to Wikipedia</a></li>
</ul>
</div>
</div>    
"""
for l in input.splitlines():
    print(l)
print(getURLName(input))