document.getElementById("get-button").onclick = fetchRoute;
document.getElementById("reset-button").onclick = reset;

nextBtn = document
  .getElementById("next")
  .addEventListener("click", function () {
    if (instructions && index < instructions.length - 1) {
      index++;
      updateInstructions();
    }
  });
prevBtn = document
  .getElementById("previous")
  .addEventListener("click", function () {
    if (instructions && index > 0) {
      index--;
      updateInstructions();
    }
  });

instructions = null;
index = 0;
distance = 0;
start = "";
destination = "";

function reset() {
  document.getElementById("start").value = "";
  document.getElementById("destination").value = "";

  document.getElementById("trip-start").textContent = "";
  document.getElementById("trip-destination").textContent = "";
  document.getElementById("trip-distance").textContent = "";
  document.getElementById("trip-duration").textContent = "";
  document.getElementById("trip-instructions").textContent = "";

  instructions = null;
  index = 0;
  distance = 0;
  start = "";
  destination = "";
}

function updateInstructions() {
  const instructionElement = document.getElementById("trip-instructions");
  const currentInstruction = instructions[index];

  const distanceText =
    currentInstruction.distance_km > 0
      ? `(${currentInstruction.distance_km} km / ${currentInstruction.distance_miles} miles)`
      : "";

  instructionElement.innerHTML = `
    ${currentInstruction.instruction} ${distanceText}
  `;
}

function fetchRoute() {
  const url = "http://localhost:8000/api/route";
  start = document.getElementById("start").value;
  destination = document.getElementById("destination").value;

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
      distance = data.distance.km;

      document.getElementById(
        "trip-start"
      ).textContent = `Start: ${data.start}`;
      document.getElementById(
        "trip-destination"
      ).textContent = `Destination: ${data.destination}`;

      document.getElementById(
        "trip-distance"
      ).textContent = `Total Distance: ${data.distance.km} km (${data.distance.miles} miles)`;
      document.getElementById(
        "trip-duration"
      ).textContent = `Total duration: ${data.duration}`;
      instructions = data.instructions;
      document.getElementById(
        "trip-instructions"
      ).textContent = `${instructions[index].instruction}`;
    })
    .catch((error) => {
      console.error("Error fetching route:", error);
      document.getElementById("trip-distance").textContent =
        "Error fetching route.";
    });
}
