# 簡易Python環境構築

## 概要
このプロジェクトはPythonを使用したサンプルアプリケーションです。Dockerを利用して環境を構築し、ローカルで容易に実行できます。

### 1. projectディレクトリについて
コンテナ起動中、`project`ディレクトリのみがコンテナ内の`/usr/src/app`にマウントされます。

これにより、`project`ディレクトリ内でのファイル編集がリアルタイムでコンテナ内に反映され、効率的な開発が可能となります。

### 2. .envファイルについて
また、プロジェクトのルートディレクトリに`.env`ファイルを追加することができます、このファイルに定義された環境変数はコンテナ内で直接参照されます。

docker-compose.ymlファイル内にenv_fileオプションを指定することで、.envファイルの内容がコンテナ起動時に自動的に読み込まれるように設定されています。

pull時に`.env`ファイルが`.gitignore`に含まれている場合、`.env`ファイルは`.gitignore`に含まれているため、`.gitignore`に`.env`を追加する必要があります。

## 前提条件
- Docker Desktopがインストールされていること。

## プロジェクトの構成
```
C:.
│  .gitignore
│  README.md
│  requirements.txt
│  .env
│
├─.docker
│      docker-compose.yml
│      Dockerfile
│
├─project
│      README.md
│      requirements.txt
│      main.py
│
└─tests
        test.py
```

## 実行手順

1. **プロジェクトのクローン**

    まず、このプロジェクトをあなたのローカルシステムにクローンします。
    ```
    git clone https://github.com/yamato-snow/Python_Dev.git <プロジェクト名>
    ```
    クローンしたディレクトリに移動します。
    ```
    cd <プロジェクト名>
    ```

2. **Dockerイメージのビルド**

    プロジェクトのルートディレクトリから、Dockerイメージをビルドします。以下のコマンドを実行してください。
    ```
    docker-compose -f .docker/docker-compose.yml build
    ```

3. **コンテナの起動**

    Dockerイメージのビルドが完了したら、コンテナを起動します。

    コンテナをバックグラウンドで実行したい場合は、コマンドに`-d`フラグを追加します。
    ```
    docker-compose -f .docker/docker-compose.yml up -d
    ```

4. **各種コマンド**

    Dockerのコンテナを確認
    ```
    docker container ls -a 
    ```

    Dockerのイメージを確認
    ```
    docker images ls -a
    ```

5. **bashの実行**

    bashの実行をするためには、次のコマンドを実行します。
    ```
    docker exec -it Docker_python bash
    ```

    bashを出る場合は、次のコマンドを実行します。
    ```
    exit
    ```

6. **各種bash内部のコマンド**

    インストールされているPythonパッケージのリストを表示
    ```
    pip list
    ```

    インストールされているPythonのバージョンを表示
    ```
    python --version
    ```

    独自のrequirements.txtファイルを使用してPythonパッケージをインストール
    ```
    pip install -r requirements.txt
    ```

    ホームに移動
    ```
    cd
    ```

    フォルダを指定して移動
    ```
    cd フォルダ名
    ```

    フォルダを階層まで指定して移動
    ```
    cd フォルダ名/フォルダ名/フォルダ名
    ```

    一つ上の階層のフォルダに移動
    ```
    cd ../
    ```

    今いるフォルダ内のファイル確認
    ```
    ls
    ```

    隠しファイルも含めて表示
    ```
    ls -a
    ```

7. **アプリケーションの停止とクリーンアップ**

    アプリケーションの実行を停止し、コンテナを削除するには、次のコマンドを実行します。
    ```
    docker-compose -f .docker/docker-compose.yml down
    ```

## 注意事項
- この手順は、プロジェクトのディレクトリ構造や設定が予め指定された通りであることを前提としています。
- 必要に応じて、`.env`ファイルを作成し、環境変数を設定してください。

以下は、`.env`ファイルを含む更新されたディレクトリ構造の例です。

```
C:.
│  .gitignore              # Gitの無視ファイルリスト
│  README.md               # プロジェクトの説明
│  requirements.txt        # 基本のPythonの依存関係リスト
│  .env                    # 環境変数設定ファイル <-- ここに配置
│
├─.docker
│      docker-compose.yml  # Docker Compose設定ファイル
│      Dockerfile          # Dockerイメージのビルド指示ファイル
│
├─project
│      main.py             # アプリケーションのメインスクリプト
│      README.md           # プロジェクトの説明
│      requirements.txt    # 独自のPythonの依存関係リスト
│
└─tests
    # テストスクリプト（ここに配置されます）
```

`.env`ファイルをプロジェクトのルートディレクトリに配置することで、`docker-compose.yml`がデフォルトでその場所から環境変数を読み込むことができます。このファイルを使用することで、データベースの接続情報、APIキー、その他の機密情報など、開発、テスト、本番環境に特有の設定を管理できます。また、`.env`ファイルはプライバシーを保護するために、バージョン管理システム（例: Git）から除外すべきです。これは、`.gitignore`ファイルに`.env`を追加することで達成できます。

### 重要:
- `.env`ファイルは機密情報を含む可能性があるため、外部に公開しないようにしてください。
- 環境ごとに異なる`.env`ファイルを持つ場合（例：`.env.production`、`.env.development`）、適切なファイルが各環境で読み込まれるように設定する必要があります。これは`docker-compose.yml`やアプリケーションの起動スクリプトで管理できます。