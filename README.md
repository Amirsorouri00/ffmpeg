# ffmpeg

## Usefull Links
* http://player.streamingtvguides.com/
* https://www.advanceddigital.com/blog/introduction-to-ffmpeg-for-broadcast-engineers/
* https://askubuntu.com/questions/999271/ffmpeg-command-for-mpeg-ts-encoding
* https://ffmpeg.org/ffmpeg-formats.html#Examples-9
* https://medium.com/@eyevinntechnology/loop-file-and-generate-multiple-video-bitrates-muxed-in-mpeg-ts-with-ffmpeg-85658d0b74bb
* https://libraries.io/search?keywords=ffmpeg&languages=Python


## Projects
* https://github.com/nyavramov/WEBMARIZER
* https://github.com/ffplayout/ffplayout-engine
* https://github.com/escaped/django-video-encoding

## Tutorial In C
* http://dranger.com/ffmpeg/tutorial01.html

## Tutorial in Python
* https://github.com/kkroening/ffmpeg-python


## Link for Installation On ubuntu
* https://linuxize.com/post/how-to-install-ffmpeg-on-ubuntu-18-04/



## Commands To Test

### One

```
$ ffmpeg -i v.mp4 -vf "drawtext=text='hellllllooooooooo there' :x=10:y=H-th-10: \
               fontfile=/path/to/font.ttf:fontsize=12:fontcolor=white: \
               shadowcolor=black:shadowx=5:shadowy=5" test.mp4
```
 
### Two
```
$ ffmpeg -i v.mp4 -i friends.jpg -filter_complex "overlay='if(gte(t,1), -w+(t-1)*200, NAN)':(main_h-overlay_h)/2" test.mp4
```

### Three
```
$ ffmpeg -i v.mp4 -vcodec mpeg2video -acodec mp3 -b:v 10M -b:a 192k -muxrate 10M -f mpegts test.ts
```

### Four
```
$ ffmpeg -re -i v.mp4        -codec copy -map 0        -f segment -segment_list playlist.m3u8        -segment_list_flags +live -segment_time 10        ./segmentedts/out%03d.ts
```

### Five
```
$ ffplay playlist.m3u8
```