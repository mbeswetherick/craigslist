from data.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import simplejson


def index(request):
	return HttpResponse(",'>/")

def create(request):
	p = request.POST
	post = Craiglistpost(price=p['price'], 
						title=p['title'], url=p['url'],
						date=p['date'], query=p['query'], 
						location_wide=p['location_wide'],
						location_region=p['location_region'],
						location_specific=p['location_specific'])
	post.save()
	return HttpResponse(simplejson.dumps(post.id))
	
def update(request, listing_id):
	if request.method == 'GET':
		g = request.GET
		#url = g['url']
		listing = Craiglistpost.object.get(id=listing_id)
		return HttpResponse(simplejson.dumps(listing.price, listing.title, listing.url, listing.date, listing.category, listing.query, listing.location_wide, listing.location_region, listing.location_specific))
	else:
		d = request.DELETE
		Craiglistpost.object.get(id=listing_id).delete()
		return HttpResponse(simplejson.dumps(listing_id))


def getStats(request):
	g = request.GET
	searched = g['search_for']
	allSearchedPosts = Craiglistpost.objects.filter(category=searched)
	if allSearchedPostS is None:
		allSearchedPosts = Craiglistpost.objects.filter(location_wide=searched)
	sumNumber = 0	
	for post in allSearchedPosts:
		sumNumber += post.price
		# have to find min and max in order to find range
	mean = sumNumber / len(allPosts)
	hasExactMean = g.get('mean_exact', None)
	numberOfPriceMatches = 0
	for post in allSearchedPosts
		if hasExactMean is not None:
			if post.price == mean
				numberOfPriceMatches += 1
		else:
			if post.price >= g['mean_min'] and post.price <= g['mean_max']	
				numberOfPriceMatches += 1
	return HttpResponse(simplejson.dumps(searched_for, numberOfPriceMatches))


def getExact(request):
	g = request.GET
	posts = []
	index = 0
	#zen
	for k,v in g:
		if k == 'price_min' or 'price_max' or 'price_max':
			pass
		else:
			posts[index] = Craiglistpost.objects.filter(k=v)
		index += 1
	#take care of price
	#if price falls in between min and max or exact price exists, put those in
	finalPosts = []
	hasExactPrice = g.get('price_exact', none)
	index = 0
	if hasExactPrice is None:
		for post in posts:
			if post.price >= g[price_min] and post.price <= g[price_max]:
				finalPosts[index] = post
			index += 1
	else:
		for post in posts:	
			if post.price == g[price_exact]:
				finalPosts[index] = post
			index += 1
	return HttpResponse(simplejson.dumps(finalPosts))			








