// Define an array of audio files in your "audio" folder
const audioFiles = ["01.mp3", "02.mp3", "03.mp3",  "04.mp3", "05.mp3", "06.mp3", "07.mp3", "08.mp3","09.mp3","10.mp3","11.mp3","12.mp3","13.mp3","14.mp3","15.mp3","16.mp3",];

const audio = document.getElementById("audio");
const shuffleBtn = document.getElementById("shuffle-btn");
const queueBtn = document.getElementById("queue-btn");
const playBtn = document.getElementById("play-btn");
const pauseBtn = document.getElementById("pause-btn");
const prevBtn = document.getElementById("prev-btn");
const nextBtn = document.getElementById("next-btn");

let currentAudioIndex = 0;

shuffleBtn.addEventListener("click", () => {
  const audioCount = audioFiles.length;
  let shuffledAudioFiles = [...audioFiles];

  // Remove the current audio from the shuffled list, if it exists
  let currentAudio = audio.src.replace(/^.*[\\\/]/, '');
  let currentAudioIndex = shuffledAudioFiles.indexOf(currentAudio);
  if (currentAudioIndex > -1) {
    shuffledAudioFiles.splice(currentAudioIndex, 1);
  }

  // Shuffle the remaining audio files
  for (let i = shuffledAudioFiles.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffledAudioFiles[i], shuffledAudioFiles[j]] = [shuffledAudioFiles[j], shuffledAudioFiles[i]];
  }

  // Play a random audio from the shuffled list
  let randomIndex = Math.floor(Math.random() * shuffledAudioFiles.length);
  currentAudioIndex = audioFiles.indexOf(shuffledAudioFiles[randomIndex]);
  playAudio(shuffledAudioFiles);
});


queueBtn.addEventListener("click", () => {
  // Play audio in the original queue order
  currentAudioIndex = 0;
  playAudio(audioFiles);
});

playBtn.addEventListener("click", () => {
  audio.play();
});

pauseBtn.addEventListener("click", () => {
  audio.pause();
});

prevBtn.addEventListener("click", () => {
  currentAudioIndex = (currentAudioIndex - 1 + audioFiles.length) % audioFiles.length;
  playAudio(audioFiles);
});

nextBtn.addEventListener("click", () => {
  currentAudioIndex = (currentAudioIndex + 1) % audioFiles.length;
  playAudio(audioFiles);
});

audio.addEventListener("ended", () => {
  // Automatically play the next audio when the current audio finishes
  currentAudioIndex = (currentAudioIndex + 1) % audioFiles.length;
  playAudio(audioFiles);
});
// ... (previous JavaScript code) ...

const playlistContainer = document.getElementById("playlist-container");
const playlist = document.getElementById("playlist");

// Generate playlist items dynamically
audioFiles.forEach((audioFile, index) => {
  const playlistItem = document.createElement("li");
  const playlistLink = document.createElement("a");
  playlistLink.textContent = audioFile.replace(/\.[^/.]+$/, ""); // Display audio name without the file extension
  playlistLink.href = "javascript:void(0)"; // Use "javascript:void(0)" to prevent page navigation
  playlistLink.addEventListener("click", () => {
    currentAudioIndex = index;
    playAudio(audioFiles);
  });
  playlistItem.appendChild(playlistLink);
  playlist.appendChild(playlistItem);
});



// ... (previous JavaScript code) ...

const audioName = document.getElementById("audio-name");

function playAudio(audioList) {
  const audioNameText = audioList[currentAudioIndex].replace(/\.[^/.]+$/, ""); // Get the audio name without the file extension
  audioName.textContent = `Now Playing: ${audioNameText}`;
  audio.src = `audio/${audioList[currentAudioIndex]}`;
  audio.play();
}

// Play the first audio when the page loads
playAudio(audioFiles);

