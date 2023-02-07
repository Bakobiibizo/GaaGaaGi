## Audio Book Generator

This is a simple script that generates an audio book from a text file. It uses the TTS Text to Speech for all library to generate the audio files. It is setup to convert the text in a README.md file into an audio book. It does this by splitting the text into individual sentences. You can use the combine.py script to combine the audio files, but since I'm an audio engineer I just combined them in Ableton and processed them with a few plugins. I've also included the project file if you're interested. Basically I just cut the harsh frequencies around 1.5khz, 3.5khz and 9khz, boosted 800hz, 2.5hkz, and 12+hkz, applied a bit of optical compression, some tube saturation, layered formant and pitch shifted versions of the audio to add some depth and I also added a bit of reverb and delay. Its not perfect but its pretty good for a few hours in one afternoon.
The model obviously needs to be fine trained. I will throw it into a TPU node tomorrow once I have organized my audio files into a suitable format. I am confident I can get a model tuned well enough to produce a reasonable product. The main goal of this is to help disseminate the foundational text of Raven not to produce a marketable TTS model, though it may be a side effect.

### Usage

**Download miniconda to create an env.**
**Linux**
`wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`
**Mac**
`wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh`
**Windows**
`https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe`

**Install**
`bash Miniconda3-latest-Linux-x86_64.sh`

**Start a new Conda environment.**
`conda create -n audio python=3.7`
This must be 3.7 because of the Tensorflow version.

**Activate the environment**
`conda activate audio`

**Install the requirements**
`pip install -r requirements.txt`

**Requirements.txt**
`python>=3.7

torch>=1.5
tensorflow==2.3.1
numpy==1.17.5
scipy>=0.19.0
numba==0.48
librosa==0.7.2
phonemizer>=2.2.0
unidecode==0.4.20
tensorboardX
matplotlib
Pillow
flask
tqdm
inflect
bokeh==1.4.0
pysbd
pyworld
soundfile
nose==1.3.7
cardboardlint==1.3.0
pylint==2.5.3
gdown
umap-learn
cython
pyyaml
pydub`

**Run the script**
`python generate.py`

**Combine the audio files**
`python combine.py`

### RESULTS OF TRAILS

## Results of the first attempt

The audio quality if fairly poor and its obvious the model needs to be fine tuned. It speaks in a very rushed fashion and does not properly pronounce acronyms. I am unsure if it would be better to phonetically write out the acronyms or to fine tune it to be able to understand the semantic difference between an acronym and a normal word. Probably easier to write a script to just replace the acronyms with a phonetic spelling.
Otherwise this went fairly well for a first attempt. I will fine tune the model tomorrow and see if I can get it to produce a better result.
You can find the first attempt [here](https://www.kaggle.com/datasets/bakobiibizo/audio-book-first-try). I am unsure, but it may be worth going through and annotating the good samples as addition data augmentation. The Vocal Processing Project is in the files and I also uploaded the audio [here](https://soundcloud.com/bakobiibizo/nlca1). The 2nd attempt with out fine tuning is running now and will be done by morning. I will process and upload the raw book tomorrow.

# Results of the second attempt

The audio quality was better on the second run, I adjusted the text to omit unpronounceable characters which reduced the amount of nonsense the model was producing. I think the links to images are messing it up still though since there was quite a few long sections of complete gibberish. I went through and got rid of most of them in the DAW(Digital Audio Work Station) and post processed the results.
[Part1](https://soundcloud.com/bakobiibizo/nlca/s-icIStVy3gOq?si=9da1554ea18742cca662db558379e42a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing)
[Part2](https://soundcloud.com/bakobiibizo/nlca2/s-CPN9aVEIBk4?si=9da1554ea18742cca662db558379e42a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing)
[Part3](https://soundcloud.com/bakobiibizo/nlca3/s-3JtqHD8mlvD?si=4c243bf8d6c54924a3de39127dfef20a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing)
Again, not amazing but at least you can listen to it. I have a model being fine tuned as I write this. Its on epoch 54 for 1000 which has already taken a while so I will run more tests once its loss rate gets closer to 1.

## TODO

- [x] Create a script to generate audio files from a text file.
- [x] Create a script to combine the audio files.
- [x] Create a script to generate a spectrogram from an audio file.
- [x] First attempt at audio book generation.
- [x] Report on the results.
- [x] Generate the complete book with out fine tuning.
- [x] Report on the results.
- [x] Prepare a training set.
- [ ] Fine tune the model.
- [ ] Generate a new audio book.
- [ ] Report on the results.
- [ ] Iterate till satisfied.
- [ ] Generate final NCLA, BbD, and SoT versions.
- [ ] Build a gui?
- [ ] Link module to raven for real time TTS when ready.


## Updates

Feb 5th 2023 - Installed the TTS requirements and wrote the scripts to generate the audio files and combine them. Processed the output and uploaded it to soundcloud.


## Credits

[TTS Text to Speech for all library](https://github.com/mozilla/TTS)

Dave Shapiro - [RAVEN OSS Community Project](https://github.com/daveshap/raven)

Materials from the following repositories:

- 'https://github.com/daveshap/NaturalLanguageCognitiveArchitecture'
- 'https://github.com/daveshap/BenevolentByDesign'
- 'https://github.com/daveshap/SymphonyOfThought'

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
