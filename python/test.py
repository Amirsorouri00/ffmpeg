import ffmpeg
import numpy as np

# (
#     ffmpeg
#     .input('FaceTime', format='avfoundation', pix_fmt='uyvy422', framerate=30)
#     .output('out.mp4', pix_fmt='yuv420p', vframes=100)
#     .run()
# )

# def test_fluent_complex_filter():
#     in_file = ffmpeg.input('v.mp4')
#     return ffmpeg.concat(
#     ).output('dummy2.mp4')

# res = test_fluent_complex_filter()
# res.run()

# in_file = ffmpeg.input('v.mp4')
# overlay_file = ffmpeg.input('friends.jpg')
# (
#    ffmpeg
#    .concat(
#        in_file.trim(start_frame=30, end_frame=4000),
#    )
#    .overlay(overlay_file.hflip())
#    .drawbox(50, 50, 120, 120, color='red', thickness=5)
#    .output('out.mp4')
#    .run()
# )




# in1 = ffmpeg.input('v.mp4')
# in2 = ffmpeg.input('v.mp4')
# v1 = in1.video.hflip()
# a1 = in1.audio
# v2 = in2.video.filter('reverse').filter('hue', s=0)
# a2 = in2.audio.filter('areverse').filter('aphaser')
# joined = ffmpeg.concat(v1, a1, v2, a2, v=1, a=1).node
# v3 = joined[0]
# a3 = joined[1].filter('volume', 0.8)
# out = ffmpeg.output(v3, a3, 'out.mp4')
# out.run()


# (
#     ffmpeg
#     .input('friends.jpg', pattern_type='glob', framerate=25)
#     .filter('deflicker', mode='pm', size=10)
#     .filter('scale', size='hd1080', force_original_aspect_ratio='increase')
#     .output('movie.mp4', crf=20, preset='slower', movflags='faststart', pix_fmt='yuv420p')
#     .view(filename='filter_graph')
#     .run()
# )



# out, _ = (
#     ffmpeg
#     .input('v.mp4')
#     .output('pipe:', format='rawvideo', pix_fmt='rgb24')
#     .run(capture_stdout=True)
# )
# video = (
#     np
#     .frombuffer(out, np.uint8)
#     .reshape([-1, 300, 300, 3])
# )

probe = ffmpeg.probe("v.mp4")
video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
width = int(video_stream['width'])
height = int(video_stream['height'])

print(video_stream, height)