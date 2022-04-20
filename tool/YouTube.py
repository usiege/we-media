from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=yyLdSexwBSQ&t=66s')
# yt.streams.get_highest_resolution().download()

yt.streams.filter(file_extension="mp4").all()

# yt.streams.get_by_itag(299).download(output_path="TBC_Ret_Paladin_VoidReaver_2900DPS_299")
# yt.streams.get_by_itag(140).download(output_path="TBC_Ret_Paladin_VoidReaver_2900DPS_140")
yt.streams.get_by_itag(299).download(output_path="TBC_Ret_Paladin_Solarian_2900DPS_299")
yt.streams.get_by_itag(140).download(output_path="TBC_Ret_Paladin_Solarian_2900DPS_140")ee