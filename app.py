from app import create_app, db

app = create_app()

with app.app_context():
    try:
        # 試著查詢資料庫
        db.session.execute('SELECT 1')
        print("✅ 資料庫連線成功！")
    except Exception as e:
        print("❌ 資料庫連線失敗：", e)

if __name__ == "__main__":
    
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
