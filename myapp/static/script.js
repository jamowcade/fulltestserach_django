
    $(document).on('submit','#search-form',function(e){
        e.preventDefault();
        let searchTerm = $('#search').val();
        let errorEl = $('.error');
        if(searchTerm == ""){
            
            errorEl.css('display','block')
            errorEl.css('color','red','font-size',20);
            errorEl.text('please type something');
            errorEl.fadeOut(7000)

        }
        else{
            // console.log(searchTerm);
            errorEl.hide()
            
            $.ajax({
                type: 'GET',
                url: "{% url 'home' %}",
                data: {
                    search:$('#search').val()
                },

                success: function(response){
                    $('tbody').empty();
                    let temp = "";
                    if(response.logs.length > 0){
                        
                        for(var log in response.logs){
                        
                        temp = `
                        <tr>
                            <td> ${response.logs[log].id}</td>
                            <td> ${response.logs[log].name}</td>
                            <td> ${response.logs[log].description}</td>
                            <td> ${response.logs[log].ip_address}</td>
                            <td> ${response.logs[log].port}</td>
                            <td> ${response.logs[log].http_response}</td>
                        </tr>
                        `;
                        $('tbody').append(temp)
                    }
                    }
                    else{
                        temp = `<p>No Data matches <b>${searchTerm}</b></p>`;
                        $('tbody').append(temp)
                       
                        
                    }
                   
                },
                error: function(response){
                    errorEl.css('display','block')
                    errorEl.css('color','red','font-size',20);
                    errorEl.text('Error: Invalid Query');
                    
                    errorEl.fadeOut(7000)
                }
            });
        }
        
        
       
           
        });
