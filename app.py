from flask import Flask, request

app = Flask(__name__)

# Homepage with a form
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get numbers from the form
        malaria = int(request.form["malaria"])
        typhoid = int(request.form["typhoid"])
        cholera = int(request.form["cholera"])

        total = malaria + typhoid + cholera
        malaria_pct = (malaria / total) * 100
        typhoid_pct = (typhoid / total) * 100
        cholera_pct = (cholera / total) * 100

        return f"""
        <h1>Health Report</h1>
        <p>Total Cases: {total}</p>
        <p>Malaria: {malaria} cases ({malaria_pct:.2f}%)</p>
        <p>Typhoid: {typhoid} cases ({typhoid_pct:.2f}%)</p>
        <p>Cholera: {cholera} cases ({cholera_pct:.2f}%)</p>
        <a href="/">Go Back</a>
        """

    return """
    <h1>Enter Health Data</h1>
    <form method="post">
        Malaria cases: <input type="number" name="malaria"><br><br>
        Typhoid cases: <input type="number" name="typhoid"><br><br>
        Cholera cases: <input type="number" name="cholera"><br><br>
        <input type="submit" value="Calculate Percentages">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)
