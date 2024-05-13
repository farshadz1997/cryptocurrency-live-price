const websocketProtocol = window.location.protocol === "https:" ? "wss" : "ws";
const websocket_url = `${websocketProtocol}://${window.location.host}/ws/coins`;
console.log(websocket_url)
const coinsWebsocket = new WebSocket(websocket_url)

coinsWebsocket.onopen = function(e) {
    console.info('Websocket connected.')
}

coinsWebsocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log(data.message);
    data.message.forEach(element => {
        update_coin(element)
    });
};

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function update_coin(coin) {
    let table_row = document.getElementById(coin.symbol);
    let table_data = table_row.getElementsByTagName('td');
    let coin_price = table_data[3];
    let market_cap = table_data[4];
    let percent_change_24h = table_data[5];
    let percent_change_7d = table_data[6];
    let percent_change_30d = table_data[7];
    
    if (coin.quote.USD.percent_change_24h >= 0) {
        percent_change_24h.style.color = 'green';
    } else {
        percent_change_24h.style.color = 'red';
    }
    
    coin_price.textContent = '$' + numberWithCommas(coin.quote.USD.price.toFixed(2));
    market_cap.textContent = numberWithCommas(coin.quote.USD.market_cap.toFixed(2));
    percent_change_24h.textContent = numberWithCommas(coin.quote.USD.percent_change_24h.toFixed(2)) + '%';
    percent_change_7d.textContent = numberWithCommas(coin.quote.USD.percent_change_7d.toFixed(2)) + '%';
    percent_change_30d.textContent = numberWithCommas(coin.quote.USD.percent_change_7d.toFixed(2)) + '%';

}