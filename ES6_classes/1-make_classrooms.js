import Classroom from './0-classroom.js';

function initializeRooms() {
  let rooms = [new Classroom(19), new Classroom(20), new Classroom(34)];
  return rooms;
}

export default initializeRooms;
