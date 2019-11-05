content = '[ti&#58;晴天]&#10;[ar&#58;周杰伦]&#10;[al&#58;叶惠美]&#10;[by&#58;]&#10;[offset&#58;0]&#10;[00&#58;00&#46;00]晴天&#32;&#45;&#32;周杰伦&#32;&#40;Jay&#32;Chou&#41;&#10;[00&#58;07&#46;34]词：周杰伦&#10;[00&#58;14&#46;69]曲：周杰伦&#10;[00&#58;22&#46;04]编曲：周杰伦&#10;[00&#58;29&#46;39]故事的小黄花&#10;[00&#58;32&#46;64]从出生那年就飘着&#10;[00&#58;36&#46;19]童年的荡秋千'
# lyric = content.replace(' ','').replace('&#10;','\n')
# print(lyric)
import re
# lyric = re.sub('[A-Za-z\d\#\&\;]','',lyric)
# lyric = lyric.replace('[','').replace(']','').replace('  ','')
# print(lyric)
# lyric = re.findall('\](.*)',lyric)
# print(lyric)
lyric = content.replace(' ','').replace('&#10;','\n')
print(lyric)
# lyric1 = re.sub('[A-Za-z\d\#\&\;]','',lyric)
# print(lyric1)
# lyric1 = re.findall('.*?](.*)',lyric1)
# lyric1 = [i for i in lyric1 if i !='']
# # for i in lyric1:
# #     if i == '':
# #         lyric1.remove(i)
# # print(lyric1)
# for i in lyric1:
#     print(i)

lyric2 = re.sub('[A-Za-z\d\#\&\;\[\]]','',lyric)
lyric2 = re.sub('[\n]{2,}','\n',lyric2)
print(lyric2)

