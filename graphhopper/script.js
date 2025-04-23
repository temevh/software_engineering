document.getElementById("get-button").onclick = fetchRoute;

function testApi() {
  fetch("http://localhost:8000/api/message")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("apiMessage").textContent = data.message;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
}

function fetchRoute() {
  const url = "http://localhost:8000/api/route";
  const start = document.getElementById("start").value;
  const destination = document.getElementById("destination").value;

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ start: start, destination: destination }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Route data:", data);

      document.getElementById(
        "trip-start"
      ).textContent = `Start: ${data.start}`;
      document.getElementById(
        "trip-destination"
      ).textContent = `Destination: ${data.destination}`;

      document.getElementById(
        "trip-distance"
      ).textContent = `Distance: ${data.distance.km} km (${data.distance.miles} miles)`;
      document.getElementById(
        "trip-duration"
      ).textContent = `Duration: ${data.duration}`;

      const instructionsList = document.getElementById("trip-instructions");
      instructionsList.innerHTML = "";
      data.instructions.forEach((instruction) => {
        const listItem = document.createElement("li");
        listItem.textContent = `${instruction.instruction} (${instruction.distance_km} km / ${instruction.distance_miles} miles)`;
        instructionsList.appendChild(listItem);
      });
    })
    .catch((error) => {
      console.error("Error fetching route:", error);
      document.getElementById("trip-distance").textContent =
        "Error fetching route.";
    });
}
