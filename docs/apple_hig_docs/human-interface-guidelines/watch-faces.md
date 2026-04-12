# 文字盤

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/watch-faces

# 文字盤

文字盤は、watchOSのプライマリビューとしてユーザが選択するビューです。

![図案化された一連のApple Watchの文字盤。画像は全体が、6色のオリジナルAppleロゴを連想させる赤色になっています。](https://docs-assets.developer.apple.com/published/e9a58a324d0bf37b1c99318ed6029816/components-faces-intro%402x.png)

文字盤はwatchOS操作環境の中核を担っています。ユーザは手首を上げる動作に合わせて表示される文字盤を選択でき、お気に入りのコンプリケーションで文字盤をカスタマイズすることもできます。そのときどきの状況に応じて最適な文字盤が表示されるように、アクティビティごとにさまざまな文字盤をカスタマイズすることも可能です。

watchOS 7以降では、自分で構成した文字盤を共有できるようになりました。例えばフィットネスインストラクターなら、「グラデーション」文字盤を選択し、色をカスタマイズして、ヘルスケアやフィットネスにおすすめのコンプリケーションを追加した文字盤を受講者と共有するという使い方が考えられます。受講者はその文字盤を自分のApple WatchやiPhoneのWatchアプリに追加するだけで、カスタマイズされた操作環境を楽しめます。自分で設定する必要はありません。

構成した文字盤をアプリ内、Webサイト上、メッセージやメールなどのアプリ経由、あるいはソーシャルメディアなどを介して共有することも可能です。文字盤を共有可能にすると、自社のコンプリケーションやアプリの普及にも役立ちます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/watch-faces#Best-practices)

**自社のコンプリケーションを取り入れた文字盤を共有して、自社アプリがユーザの目に触れる機会を増やす。** 複数のコンプリケーションに対応して、それらが目立つようにした文字盤を共有し、選りすぐりの操作性を提供できれば理想的です。システムのアクセントカラーや、画像、スタイルを指定できる文字盤もあります。ユーザが文字盤を追加した時点で対応のアプリをまだインストールしていない場合は、インストールを促すメッセージがシステムから表示されます。

**共有する各文字盤のプレビューを提示する。** 文字盤の魅力を強調するプレビューを見せれば、ユーザは文字盤のメリットを視覚的にイメージしやすくなります。プレビューを取得するには、iOSのWatchアプリから文字盤をメールで自分宛に送信します。プレビューには文字盤を囲むデバイスベゼルのイラストが含まれ、これをWebサイトやwatchOSおよびiOSのアプリで効果的に表示できます。ベゼルのイラストの代わりに、[Appleデザインリソース](https://developer.apple.com/design/resources/#product-bezels)からハードウェアベゼルの高画質画像をダウンロードして、プレビューと合成することもできます。デベロッパ向けのガイダンスは、[Apple Watch文字盤を共有する](/documentation/ClockKit/sharing-an-apple-watch-face)を参照してください。

**文字盤を共有する場合はApple Watchの全世代をカバーすることを目指す。** 一部の文字盤は利用できる世代が限定されています。例えば、カリフォルニア、クロノグラフプロ、グラデーション、インフォグラフ、インフォグラフモジュラー、メリディアン、モジュラーコンパクト、ソーラーダイヤルはSeries 4以降、エクスプローラーはSeries 3（Cellularモデル）以降でしか使えません。このいずれかをベースに文字盤を作った場合は、Series 3以前のモデルにも対応した文字盤を使って似たような構成を提供することを検討してください。ユーザが選びやすいように、共有する各文字盤には対応デバイスを明記してください。

**互換性のない文字盤を選んだユーザに適切に対応する。** Series 3以前のモデルで、互換性のない文字盤を使おうとすると、システムからアプリにエラーが通知されます。こうした場合には、ただエラーを表示するのではなく、互換性のある文字盤を使った代わりの構成が即座に提供されるように努めてください。また、選んだ文字盤がApple Watchと互換性がなかった場合に代わりの文字盤が提供される可能性について、プレビューを提供する際にユーザに説明してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/watch-faces#Platform-considerations)

 _iOS、iPadOS、macOS、tvOS、visionOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/watch-faces#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/watch-faces#Related)

[Appleデザインリソース — 製品ベゼル](https://developer.apple.com/design/resources/#product-bezels)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/watch-faces#Developer-documentation)

[Apple Watchの文字盤を共有する](/documentation/ClockKit/sharing-an-apple-watch-face) — ClockKit
