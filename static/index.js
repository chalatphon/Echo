
function AddData(){
  var _event = document.getElementById("event").value;
  var _routine = document.getElementById("routine").value;
  var _date = document.getElementById("date").value;
  const var_date = new Date(_date)
  var calendarevent = {
    "id": "wad7r4w3",
    "name": "dwdwdiuj2",
    "date": "October/17/2023",
    "type": "holiday",
  }
  globalThis (calendarevent)
  var jsoncalendar_event = JSON.stringify(calendarevent);
  globalThis (jsoncalendar_event)
  console.log(typeof jsoncalendar_event);

}
$("#calendar").evoCalendar({
    calendarEvents: [
  {
    id: "fewf28few", // Event's ID (required)
    name: "Kinh", // Event name (required)
    date: "October/25/2023", // Event date (required)
    type: "holiday", // Event type (required)
    everyYear: true // Same event every year (optional)
  },
  {
    id: 'bHay68s', // Event's ID (required)
    name: "Kingkong day's", // Event name (required)
    date: "October/17/2023", // Event date (required)
    type: "holiday", // Event type (required)
    everyYear: true // Same event every year (optional)
  },
  jsoncalendar_event
  ]
});
