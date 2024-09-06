     // 
     var modal = document.getElementById("addEmployeeModal");

     // Get the button that opens the modal
     var btn = document.getElementById("addEmployeeBtn");

     // Get the <span> element that closes the modal
     var span = document.getElementById("closeModal");

     // When the user clicks the button, open the modal
     btn.onclick = function() {
         modal.style.display = "block";
     }

     // When the user clicks on <span> (x), close the modal
     span.onclick = function() {
         modal.style.display = "none";
     }

     // When the user clicks anywhere outside of the modal, close it
     window.onclick = function(event) {
         if (event.target == modal) {
             modal.style.display = "none";
         }
     }

    //  This tab is for the opening of tab of each panels 

    function opentab (evt, tabName) {
        var i , tabcontent, tablinks;
        tabcontent = document.getElementsByClassName("tabcontent");
        for (i = 0; i < tabcontent.length; i++){
            tabcontent[i].style.display = "none";
        }  tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }
        document.getElementById(tabName).style.display = "block";
        evt.currentTarget.className += " active";
    }
    
    document.addEventListener('DOMContentLoaded', (event) => {
        document.getElementById("defaultOpen").click();
    });
     