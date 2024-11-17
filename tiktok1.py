from collections import Counter
import re

def trendingHashtags(comments):
  hashtags = []
  for comment_list in comments:
      for comment in comment_list:
          hashtags.extend(re.findall(r"#\w+", comment.lower()))
  most_common = Counter(hashtags).most_common()
  most_common.sort(key=lambda x: (-x[1], x[0]))
  return [tag for tag, _ in most_common[:3]]

print(trendingHashtags([
["Enjoy our latest comedy skit! #funy #summer"],
["Unwind at the beach with our travel guide #summer #beach #funny"],
["Catch the sunset in our evening vlog #funny #beach #sunset"]
 ]))
