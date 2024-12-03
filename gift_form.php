<!DOCTYPE html>
<html>
<body>
    <h1>Gift Selection Form</h1>
    <form action="http://<python-app-instance-public-ip>/result" method="get">
        <label for="gifts">Select gifts (comma-separated indices):</label>
        <input type="text" id="gifts" name="selection">
        <button type="submit">Submit</button>
    </form>
</body>
</html>
