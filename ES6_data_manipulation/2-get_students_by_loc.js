export default function getStudentsByLocation(arr, location) {
  return arr.filter((x) => x.location === location)
}
