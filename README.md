# Syakyo Full Stack FastAPI Template

SYAKYO https://github.com/fastapi/full-stack-fastapi-template

FastAPIとReactを使用したフルスタックWebアプリケーションのテンプレートプロジェクト。
オリジナル: https://github.com/fastapi/full-stack-fastapi-template

## 概要

このプロジェクトは、現代的なフルスタックWebアプリケーション開発のベストプラクティスを学習するための実装プロジェクトです。ユーザー認証、アイテム管理、CRUD操作などの基本的な機能を含んでいます。

## 主な機能

- ユーザー認証（サインアップ、ログイン、パスワード変更）
- アイテム管理（作成、読み取り、更新、削除）
- レスポンシブなUIデザイン
- リアルタイムAPIクライアント生成
- データベースマイグレーション
- E2Eテスト

## Tech Stack

### Frontend
- **React** - UIライブラリ
- **TypeScript** - 型安全性
- **Vite** - ビルドツール
- **Chakra UI** - コンポーネントライブラリ
- **TanStack Router** - ルーティング
- **TanStack Query** - データフェッチング
- **React Hook Form** - フォーム管理

### Backend
- **FastAPI** - Webフレームワーク
- **SQLModel** - ORM（SQLAlchemyベース）
- **Pydantic** - データバリデーション
- **PostgreSQL** - データベース
- **Alembic** - データベースマイグレーション
- **JWT** - 認証
- **bcrypt** - パスワードハッシュ化

### 開発ツール
- **Docker** - コンテナ化
- **uv** - Pythonパッケージマネージャー
- **Playwright** - E2Eテスト
- **Biome** - フロントエンドのフォーマッタ・リンター
- **Ruff** - Pythonのフォーマッタ・リンター

## プロジェクト構造

```
├── backend/                 # FastAPI バックエンド
│   ├── app/
│   │   ├── api/            # APIルート
│   │   ├── core/           # 設定・セキュリティ
│   │   ├── database/       # データベースリポジトリ
│   │   └── model/          # データモデル
│   ├── migrations/         # Alembicマイグレーション
│   └── pyproject.toml      # Python依存関係
├── frontend/               # React フロントエンド
│   ├── src/
│   │   ├── client/         # 自動生成APIクライアント
│   │   ├── components/     # Reactコンポーネント
│   │   ├── hooks/          # カスタムフック
│   │   └── routes/         # ページルート
│   └── package.json        # Node.js依存関係
├── scripts/                # スクリプト
└── docker-compose.yml      # Docker設定
```

## セットアップ手順

### 必要な環境

- Python 3.11+
- Node.js 18+
- Docker & Docker Compose
- uv (Python パッケージマネージャー)

### 1. リポジトリをクローン

```bash
git clone <repository-url>
cd syakyo-full-stack-fastapi-template
```

### 2. 環境変数の設定

プロジェクトルートに `.env` ファイルを作成：

```bash
# Database
POSTGRES_SERVER=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=app

# Application
PROJECT_NAME="Syakyo Full Stack App"
BACKEND_CORS_ORIGINS=["http://localhost:5173"]
```

### 3. データベースを起動

```bash
docker-compose up -d db
```

### 4. バックエンドの設定

```bash
cd backend

# uvをインストール（未インストールの場合）
pip install uv

# 依存関係をインストール
uv sync

# データベースマイグレーション
uv run alembic upgrade head

# サーバーを起動
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. フロントエンドの設定

新しいターミナルで：

```bash
cd frontend

# 依存関係をインストール
npm install

# APIクライアントを生成
../scripts/generate-client.sh

# 開発サーバーを起動
npm run dev
```

## 開発環境の起動

### APIクライアントの更新

バックエンドのAPIを変更した場合、フロントエンドのクライアントを再生成：

```bash
./scripts/generate-client.sh
```

### データベースマイグレーション

新しいマイグレーションファイルを作成：

```bash
cd backend
uv run alembic revision --autogenerate -m "マイグレーション名"
uv run alembic upgrade head
```

### テストの実行

```bash
# バックエンドテスト
cd backend
uv run pytest

# E2Eテスト
cd frontend
npx playwright test
```

## アクセス

- フロントエンド: http://localhost:5173
- バックエンドAPI: http://localhost:8000
- API ドキュメント: http://localhost:8000/docs
- データベース: localhost:5432

## 開発ワークフロー

1. バックエンドでAPIを実装
2. `generate-client.sh` を実行してクライアントを更新
3. フロントエンドでUIを実装
4. テストを作成・実行
5. コードのフォーマット・リンターを実行

## ライセンス

MIT License - 詳細は [LICENSE](LICENSE) ファイルを参照
