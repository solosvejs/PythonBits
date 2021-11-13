#Description: Takes a user-provided list of AO3 tags and creates an HTML file with clickable links so you can open the tags quickly.
#Requirements: Standard Python 3 library
#===================================#

#empty list to store tags
tagList = []

def make_tag_urls(tags):
	#use the list to generate ao3 edit page urls
		if tags == 'x':
			print()
			print('Bye! o(*￣▽￣*)ブ')
			exit()

		else:
			tagList = tags.split(', ')
			print('Generating URLs...')
			url = 'https://archiveofourown.org/tags/'
			edit = '/edit'
			tagUrls = list(map(lambda tag: url + tag + edit, tagList))

			#add the html tags:
			tag_a = list(map(lambda link: f'<a href="{link}">{link}</a><br>',tagUrls))
			print(tag_a)

			#output to an html file
			with open('tags.html', 'w') as f:
				f.writelines(tag_a)

			print('Done! Check the folder for an HTML file!')

def main():
	print('Oh no did you accidentally shovel fandom tags into NF? (╯O A O)╯︵┻━┻ \n This will create clickable links from the blurb confirmation at the top (or any other list of tags) so you can get them back easily! \n ')
	while True:
		tags = input('Paste your tags here, separated by COMMAS, or type x to exit: ')
		make_tag_urls(tags)
		print()
main()





