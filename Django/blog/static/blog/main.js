// post_detail.html

const post_detail = document.querySelector(".thumbs-up-link");
post_detail.addEventListener("click", function(event){
    console.log(event.currentTarget);
    event.preventDefault()
})