from flask import Blueprint, render_template,request, jsonify,redirect,url_for
from app.extensions import db

recommend_bp = Blueprint('recommend', __name__)

@recommend_bp.route("/recommend",methods=["GET", "POST"])
def recommend():
    if request.method == "POST":
        name = request.form["name"]
        url = request.form["url"]
        description = request.form.get("description", "")
        image = request.form.get("image", "")
        if not name or not url:
            return jsonify({"error": "Name and URL are required"}), 400
        if not url.startswith("http://") and not url.startswith("https://"):
            return jsonify({"error": "URL must start with http:// or https://"}), 400
        if not image:
            image = "default_image.png"
        if not description:
            description = "No description provided"
        # Create a new recommended site entry
        from app.models import RecommendedSite
        new_site = RecommendedSite(name=name, url=url, description=description, image=image)
        db.session.add(new_site)
        db.session.commit()
        return redirect(url_for("recommend.recommend"))

    
    # Fetch all recommended sites
    from app.models import RecommendedSite
    all_sites = RecommendedSite.query.all()
    return render_template("recommend.html", sites=all_sites)

@recommend_bp.route("/recommend/delete/<int:stie_id>", methods=["GET", "POST"])
def delete_site(site_id):
    from app.models import RecommendedSite
    site = RecommendedSite.query.get_or_404(site_id)
    db.session.delete(site)
    db.session.commit()
    return redirect(url_for("recommend.recommend"))