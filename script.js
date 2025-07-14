import { WORD_LIST } from './words.js';

const NUMBER_OF_GUESSES = 6;
const WORD_LENGTH = 5;

const targetWord = WORD_LIST[Math.floor(Math.random() * WORD_LIST.length)].toUpperCase();

// Example word for tests
// const targetWord = 'CRANE';

let currentGuess = '';
let currentRow = 0;

document.addEventListener('DOMContentLoaded', () => {
  createBoard();
  createKeyboard();
});

function createBoard() {
  const board = document.getElementById('game-board');
  for (let i = 0; i < NUMBER_OF_GUESSES; i++) {
    const row = document.createElement('div');
    row.className = 'row';
    row.id = `row-${i}`;
    for (let j = 0; j < WORD_LENGTH; j++) {
      const tile = document.createElement('div');
      tile.className = 'tile';
      tile.id = `row-${i}-tile-${j}`;
      row.appendChild(tile);
    }
    board.appendChild(row);
  }
}

function createKeyboard() {
  const keys = [
    ['Q','W','E','R','T','Y','U','I','O','P'],
    ['A','S','D','F','G','H','J','K','L'],
    ['Enter','Z','X','C','V','B','N','M','←']
  ];

  keys.forEach((keyRow, rowIndex) => {
    const rowEl = document.getElementById(`kb-row-${rowIndex + 1}`);
    keyRow.forEach(key => {
      const button = document.createElement('button');
      button.textContent = key;
      button.classList.add('key');
      if (key === 'Enter' || key === '←') {
        button.classList.add('wide');
      }
      button.addEventListener('click', () => handleKeyPress(key));
      rowEl.appendChild(button);
    });
  });
}

function handleKeyPress(key) {
  if (key === 'Enter') {
    if (currentGuess.length === WORD_LENGTH) {
      checkGuess();
    }
    return;
  }

  if (key === '←') {
    if (currentGuess.length > 0) {
      currentGuess = currentGuess.slice(0, -1);
      updateTiles();
    }
    return;
  }

  if (currentGuess.length < WORD_LENGTH && /^[A-Z]$/.test(key)) {
    currentGuess += key;
    updateTiles();
  }
}

function updateTiles() {
  for (let i = 0; i < WORD_LENGTH; i++) {
    const tile = document.getElementById(`row-${currentRow}-tile-${i}`);
    tile.textContent = currentGuess[i] || '';
  }
}

function checkGuess() {
  const guess = currentGuess.toLowerCase();
  const rowTiles = [];

  if (!WORD_LIST.includes(guess)) {
    alert('❌ Not a valid word.');
    return;
  }

  const upperGuess = guess.toUpperCase();

  for (let i = 0; i < WORD_LENGTH; i++) {
    const tile = document.getElementById(`row-${currentRow}-tile-${i}`);
    const letter = upperGuess[i];
    tile.textContent = letter;

    if (letter === targetWord[i]) {
      tile.classList.add('correct');
    } else if (targetWord.includes(letter)) {
      tile.classList.add('present');
    } else {
      tile.classList.add('absent');
    }

    rowTiles.push(tile);
  }

  if (upperGuess === targetWord) {
    setTimeout(() => alert('🎉 You guessed it!'), 100);
  } else if (currentRow === NUMBER_OF_GUESSES - 1) {
    setTimeout(() => alert(`🔚 Out of guesses. Word was: ${targetWord}`), 100);
  }

  currentGuess = '';
  currentRow++;
}