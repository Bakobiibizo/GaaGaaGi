from pydub import AudioSegment
import os

def combine_audio_files():
    # Get a list of all the chunk files in the out directory
    chunks = [f for f in os.listdir('./out') if f.startswith('chunk_')]

    # Sort the chunks based on their chunk number
    chunks.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

    # Load the first chunk
    combined = AudioSegment.from_wav(f'./out/{chunks[0]}')

    # Iterate over the rest of the chunks and concatenate them
    for chunk in chunks[1:]:
        combined += AudioSegment.from_wav(f'./out/{chunk}')

    # Save the combined audio to a single file
    combined.export('./out/combined.wav', format='wav')

combine_audio_files()