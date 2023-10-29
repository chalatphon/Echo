
$("#calendar").evoCalendar({
    theme:"Royal Navy",
    calendarEvents: [
  {
    id: 'bHay68s', // Event's ID (required)
    name: "Sunsu", // Event name (required)
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
  {
    id: 'bHay68s',
    badge: "02/13 - 02/15", // Event badge (optional)
    date: ["February/13/2020", "February/15/2020"], // Date range
    description: "Vacation leave for 3 days.", // Event description (optional)
    type: "event",
    color: "#63d867" // Event custom color (optional)
  }
    ],
});
function AddData(){
    var _event = document.getElementById("event").value;
    var _routine = document.getElementById("routine").value;
    var _date = document.getElementById("date").value;
    const var_date = new Date(_date)
    console.log(var_date);
    // var datalist;
    // if (localStorage.getItem("datalist") == null) {
    //     datalist = [];
    // } else {
    //     datalist = JSON.parse(localStorage.getItem("datalist")) 
    // }
    // datalist.push({
    //     _event: _event,
    //     _routine: _routine,
    // });

    // localStorage.setItem("datalist", JSON.stringify
    // (datalist));
    // showData();
    // document.getElementById("_event").value = "";
    // document.getElementById("_routine").value = "";
}

