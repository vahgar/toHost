<script>

    $(document).ready(function(){
        $('#section1').click(function() {
            $('#inside_section1').slideToggle("slow");
        });

        $('#section1').hover(function() {
            $('#section1').css('background-color','#bf7fbf')

        },function() {

            $('#section1').css('background-color','')

        });

        $(document).click(function(e) {
         if(e.target.id!="section1")
         {
            $("#inside_section1").slideUp("slow");
         }
         if(e.target.id!="section2_")
         {
            $('#inside_section2_').slideUp("slow");
         }
        });

        $('#section2_').click(function() {
            $('#inside_section2_').slideToggle("slow");
        });

        $('#section2_').hover(function() {
            $('#section2_').css('background-color','#bf7fbf')

        },function() {

            $('#section2_').css('background-color','')

        });


    });
        

    </script>



    <script>

    $(document).ready(function(){
        $('#section1_').click(function() {
            $('#inside_section1_').slideToggle("slow");
        });

        $('#section1_').hover(function() {
            $('#section1_').css('background-color','#bf7fbf')

        },function() {

            $('#section1_').css('background-color','')

        });

        $(document).click(function(e) {
         if(e.target.id!="section1_")
         {
            $("#inside_section1_").slideUp("slow");
         }
         if(e.target.id!="section2_")
         {
            $('#inside_section2_').slideUp("slow");
         }
        });

        $('#section2_').click(function() {
            $('#inside_section2_').slideToggle("slow");
        });

        $('#section2_').hover(function() {
            $('#section2_').css('background-color','#bf7fbf')

        },function() {

            $('#section2_').css('background-color','')

        });


    });

    </script>