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

'''
def getStats(request):
	g = request.GET
	mean_min = g['mean_min']
	mean_max = g['mean_max']
	mean_exact = g['mean_exact']
	median_min = g['median_min']
	median_max = g['median_max']
	median_exact = g['median_exact']
	range_min = g['range_min']
	range_max = g['range_max']
	search_for = g['search_for']
	allPosts = Craiglistpost.objects.filter(category=search_for)
	category = search_for
	if mean_exact is not None:
		mean_exact_counter = 0
		for post in allPosts:
			if
'''

def getExact(request):
	g = request.GET
	price_min = g['price_min']
	price_max = g['price_max']
	price_exact = g['price_exact']
	title = g['title']
	date_before = g['date_before']
	date_after = g['date_after']
	category g['category']
	location_wide = g['location_wide']
	location_region = g['location_region']
	location_specific = g['location_specific']
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
	for attribute in query:
		posts[0] = Craiglistpost.objects.filter(attribute		
	








