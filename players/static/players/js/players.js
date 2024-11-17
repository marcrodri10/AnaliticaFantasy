const PATH = new URL(window.location.href)
let currentPage = PATH.searchParams.get("page")
const previousBtn = document.querySelector(".previous")
const main = document.querySelector("#main")
const nextBtn = document.querySelector(".next")
const searchInput = document.querySelector("#search")
let interval, searchedPlayers;

if(currentPage == null) currentPage = 1
if(currentPage == 1) previousBtn.disabled = true

const allPlayers = await getAllPlayers();

searchInput.addEventListener("input", (event) => {
  clearInterval(interval)
  interval = setTimeout(() => {
    if(event.target.value != "") {
      searchedPlayers = allPlayers.players.filter(player => player.nickname.toLowerCase().includes(event.target.value))
      document.querySelector(".pagination").style.visibility = "hidden"
    }
    else {
      searchedPlayers = searchedPlayers = allPlayers.players
      document.querySelector(".pagination").style.visibility = "visible"
    }
    
    renderPlayers(searchedPlayers, 60)

  }, 500)
})

nextBtn.addEventListener("click", async () => {
    const players = await getPlayers(currentPage + 1)
    currentPage = currentPage + 1
    renderPlayers(players.players)
    if(currentPage != 1 ) previousBtn.disabled = false
    if(currentPage >= 10) nextBtn.disabled = true
})
previousBtn.addEventListener("click", async () => {
    const players = await getPlayers(currentPage - 1)
    currentPage = currentPage - 1
    renderPlayers(players.players)
    if(currentPage != 1 ) previousBtn.disabled = false
    if(currentPage >= 10) nextBtn.disabled = true
})

async function getAllPlayers() {
  try {
      const response = await fetch("/players/get/");
      if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      return data; // Devolvemos los datos para que puedan ser usados en el resto del código
  } catch (error) {
      console.error('Error fetching players:', error);
  }
}
async function getPlayers(currentPage) {
    try {
        const response = await fetch("/players/api/?page="+currentPage);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        return data; // Devolvemos los datos para que puedan ser usados en el resto del código
    } catch (error) {
        console.error('Error fetching players:', error);
    }
}


function createPlayerHTML(player) {
    const statusIcons = {
      ok: '/static/players/img/tick.svg',
      injured: '/static/players/img/injured.svg',
      suspended: '/static/players/img/suspended.svg',
      doubtful: '/static/players/img/doubtful.svg'
    };
  
    const statusTexts = {
      ok: 'Alineable',
      injured: 'Lesionado',
      suspended: 'Suspendido',
      doubtful: 'Dudoso'
    };
    const positions = {
        1: "POR",
        2: "DEF",
        3: "CEN",
        4: "DEL",
        5: "ENT"
    }
    return `
      <div class="player-wrapper">
        <div class="player">
          <div class="player-images">
            <img
              src="${player.images.transparent['256x256']}"
              alt=""
              class="player-image"
            />
            <img src="${player.team.badgeColor}" class="player-team-image" />
          </div>
          <div class="player-data-wrapper">
            <div class="player-data">
              <div class="player-left">
                <div class="player-name">
                  <p class="position-${positions[player.positionId]}">${positions[player.positionId]}</p>
                  <p>${player.nickname}</p>
                </div>
                <div class="status">
                  <img src="${statusIcons[player.playerStatus]}" alt="${player.playerStatus}" class="svg">
                  <p>${statusTexts[player.playerStatus]}</p>
                </div>
                <div class="market-value">
                  <img src="/static/players/img/euro.svg" alt="euro" class="svg">
                  <p>${parseFloat(player.marketValue).toLocaleString('es-ES')}</p>
                </div>
              </div>
              <div class="player-right">
                <p class="font-20"><span class="gray-text font-12">PFSY: </span> ${player.points}</p>
                <p class="font-12"><span class="gray-text font-12">MEDIA: </span> ${player.averagePoints.toFixed(2)}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;
  }
  function renderPlayers(players, total=null) {
    const playersWrapper = document.getElementById('players-wrapper');
    playersWrapper.innerHTML = ''; // Limpiar contenido anterior
    if(total != null){
      players.forEach((player, index) => {
        if(index < total) playersWrapper.innerHTML += createPlayerHTML(player);
      });
    }
    else {
      players.forEach((player, index) => {
        playersWrapper.innerHTML += createPlayerHTML(player);
      });
    }
    
  }
