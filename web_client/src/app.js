var myApp = angular.module('myApp', [])
myApp.controller('myController', function($scope) {
    var slide =  function(){
            this.content = ''
    this.wiki=false}

    $scope.activityMessage = "";
    $scope.isLoading = false

    $scope.title = ""

    $scope.author = ""

    $scope.backend = "impress"

    $scope.slides = [new slide()]  ;

    $scope.add_slide = function(){

        $scope.slides.push(new slide())
        //$scope.$apply()
    }

    $scope.remove_slide = function(slide_index){

        $scope.slides.splice(slide_index, 1);
        //$scope.$apply()
    }

    $scope.apply = function() {
        var paragraphs = []
        var slides = $scope.slides
        for (index = 0; index < slides.length; ++index) {
             var content = ""
             if (slides[index].wiki == true) { content = "WIKI:"}
             content += slides[index].content
             paragraphs.push(content)
         }

        var slides =  {"title": $scope.title, "author": $scope.author,
                    "paragraphs" : paragraphs, "backend": $scope.backend}

        slides = JSON.stringify(slides)
        //alert ("request data "+ slides)
        $scope.activityMessage = "wait while generating slides ....";
        $scope.isLoading = true
        $.ajax({
            url: '/slides_data',
            type: 'post',
            data: JSON.stringify(slides, null, '\t'),
            contentType: 'application/json;charset=UTF-8',

            success: function (data) {
                hideAnimation()
                $scope.isLoading = false
                $scope.$apply()

                alert("success!!!!!");

                get_presentation()
            }

        });




    }

    var hideAnimation = function()
    {
        $scope.activityMessage = '';

    }

    function get_presentation()      {
        $('#downloadFrame').remove(); // This shouldn't fail if frame doesn't exist
        $('body').append('<iframe id="downloadFrame" style="display:none"></iframe>');
        $('#downloadFrame').attr('src','/my_presentation    ');

    }



    }   )

myApp.directive('activity', [
    function () {
        var template = '<div class="activity-box" > <img src="working.gif" width="200" /><span>{{ message }}</span> </div>'
        return {
            restrict: 'EA',
            template: template,
            replace: true,
            scope: {
                message: '@'
            },
            link: function (scope, element, attrs) {}
        };
    }
]);