<html>

    <head>
        <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">
        <style>
            #population-table {
                width        : 30%;
                margin-left  : auto;
                margin-right : auto;
            }
        </style>
    </head>

    <body>
        <table class="table table-bordered" id="population-table">
            <thead>
                <th>Country</th>
                <th>Population</th>
            </thead>

            <tbody>
            {% for country in countries %}
                <tr>
                    <td>{{ country.name }}</td>
                    <td>{{ country.population}}</td>
                </tr>
            {% endfor %}
            </tbody>
        </table>
    </body>

</html>
