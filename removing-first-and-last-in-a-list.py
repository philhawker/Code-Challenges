
def remove_first_and_last(list_to_clean):
  _, *content, _ = list_to_clean    # *content is globbing. grabbing everything inbetween the first and last
  return content                        # underscores _ "" _ are there to show that something is going to be removed. not required syntax


html = ['<h1>', 'My content', '</h1>']

print(remove_first_and_last(html))

other_content_to_clean = ['', 'My content', 'Something else', '/']

print(remove_first_and_last(other_content_to_clean))
