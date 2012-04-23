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
	mean_min = g.get('mean_min', None)
	mean_max = g.get('mean_max', None)
	mean_exact = g.get('mean_exact', None)
	median_min = g.get('median_min', None)
	median_max = g.get('median_max', None)
	median_exact = g.get'median_exact', None)
	range_min = g.get('range_min', None)
	range_max = g.get('range_max', None)
	search_for = g.get('search_for', None)
	allPosts = Craiglistpost.objects.filter(category=search_for)
	category = search_for
	if mean_exact is not None:
		mean_exact_counter = 0
		for post in allPosts:
			if


def getExact(request):
	g = request.GET
	posts = []
	index = 0
	#zen
	for k,v in g:
		posts[index] = Craiglistpost.objects.filter(k=v)
		index += 1
	return HttpResponse(simplejson.dumps(posts))			



	'''	SHITTY CODE
	price_min = g.get('price_min', None)
	price_max = g.get('price_max', None)
	price_exact = g.get('price_exact',None)
	title = g.get('title',None)
	date_before = g.get('date_before', None)
	date_after = g.get('date_after', None)
	category = g.get('category', None)
	location_wide = g.get('location_wide', None)
	location_region = g.get'location_region', None)
	location_specific = g.get('location_specific', None)
	#to see which ones are actually filled out
	filledOut = [price_min, price_max, price_exact, title, date_before, date_after, category, location_wide, location_region, location_specific]
	query = []
	index = 0
	#check to see which ones are filled out
	for attribute in filledOut:
		attribute is not None:
			query[index] = attribute
		index += 1
	#allPosts = Craiglistpost.objects.filter(category=search_for)
	posts = []
	index = 0
	keys = g.keys()
	for attribute in query:
	'''







