function addStar (placer) {
    const star = document.createElement('div');
    star.className = 'bi-star-fill';
    placer.appendChild(star);
    }

function addHalfStar (placer) {
    const half_star = document.createElement('div');
    half_star.className = 'bi-star-half';
    placer.appendChild(half_star);
    }

function addHollowStar (placer) {
    const hollow_star = document.createElement('div');
    hollow_star.className = 'bi-star';
    placer.appendChild(hollow_star);
    }

function createN (id, n){
    const placer = document.getElementById(id);

    for (let i = 0; i < Math.floor(n); i++){
        addStar(placer);
        }
    if (n - Math.floor(n) != 0) {
        addHalfStar(placer);
        }
    for (let i = 0; i < 5-Math.ceil(n); i++){
        addHollowStar(placer);
        }
    }