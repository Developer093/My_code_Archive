let count = 1;

function plus() {
    count++;

    document.getElementById("count").textContent = count;
}

function minus() {

    if (count > 1) {
        count--;

        document.getElementById("count").textContent = count;
    }

}