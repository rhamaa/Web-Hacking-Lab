 <?php

if(isset($_POST["url"])){
   $url = $_POST['url'];

    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER,1);
    curl_setopt($curl, CURLOPT_TIMEOUT, 5);
    curl_setopt($curl, CURLOPT_CONNECTTIMEOUT, 5);

    $data = curl_exec ($curl);

    if(curl_error($curl)){
        die(curl_error($curl));
    }
    curl_close ($curl);
}
?> 

<!DOCTYPE html>
<html>
<head>
	<title>Fetch Page</title>
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<link rel="icon" href="/img/favicon.ico">

<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
<script src="https://code.jquery.com/jquery-1.11.1.min.js"></script>

</head>
<body>

<div class="container" style="margin-top: 8%;">
<div class="col-md-6 col-md-offset-3">     
<div class="row">
<div id="logo" class="text-center">
<h1>Web Page Fetch</h1>
</div>
<form action="" method="POST" role="form" id="form-buscar" enctype="multipart/form-data">
<div class="form-group">
<div class="input-group">
<input id="1" class="form-control" type="text" name="url" placeholder="URL..." required/>
<span class="input-group-btn">
<button class="btn btn-success" type="submit"><i class="glyphicon glyphicon-fetch" aria-hidden="true"></i>Fetch</button>
</span>
</div>
</div>
</form>

<div class="form-group">
  <label for="comment">Response:</label>
  <textarea class="form-control" rows="5" id="response"><?php echo (isset($data)) ? $data : '' ?></textarea>
</div>
</div>            
</div>
</div>

</body>
</html>
