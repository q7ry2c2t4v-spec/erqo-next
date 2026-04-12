# ゲーム向けのデザイン

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/designing-for-games

# ゲーム向けのデザイン

Appleデバイスでゲームをプレイするとき、ユーザは、好きなプラットフォームの機能を頼りにしながら、デザインされた世界に飛び込みます。

![図案化されたゲームコントローラ。グリッドの一番上に表示されています。画像の上に長方形と円形のグリッド線が重ねられており、画像全体が6色の初代Appleロゴの緑を連想させる緑色を帯びています。](https://docs-assets.developer.apple.com/published/87a9000504347b999d742d13b3b73635/platforms-games-intro%402x.png)

Appleプラットフォームに合わせてゲームを作成したり適応させたりする際には、基本的なプラットフォームの特徴やパターンを統合する方法について理解しておくと、どのAppleデバイスにもなじむゲームを構成するのに役立ちます。それぞれのプラットフォームをユニークなものにする要因について詳しくは、[iOS向けのデザイン](/jp/design/human-interface-guidelines/designing-for-ios)、[iPadOS向けのデザイン](/jp/design/human-interface-guidelines/designing-for-ipados)、[macOS向けのデザイン](/jp/design/human-interface-guidelines/designing-for-macos)、[tvOS向けのデザイン](/jp/design/human-interface-guidelines/designing-for-tvos)、[visionOS向けのデザイン](/jp/design/human-interface-guidelines/designing-for-visionos)、および[watchOS向けのデザイン](/jp/design/human-interface-guidelines/designing-for-watchos)を参照してください。デベロッパ向けのガイダンスは、[Games Pathway](https://developer.apple.com/games/pathway/)を参照してください。

## [ゲームプレイをすぐに開始する](/jp/design/human-interface-guidelines/designing-for-games#Jump-into-gameplay)

**インストールの完了後、すぐにプレイできるようにする。** プレイヤーのゲームの初めての体験を、長々と続くダウンロードを待つような体験にしてはいけません。ゲームの初回インストールにできるだけ多くのプレイ可能なコンテンツを含め、ダウンロードが30分以内に終わるようにしましょう。追加のコンテンツは、バックグラウンドでダウンロードします。ガイダンスは[読み込み](/jp/design/human-interface-guidelines/loading)を参照してください。

**最適なデフォルト設定を提供する。** 最初に多くの設定を変更しなくても、すぐにプレイを開始できると、プレイヤーに喜ばれます。プレイヤーのデバイスに関する情報を使用して、ゲームに最適なデフォルトを選んでください。例えば、デバイスの解像度の情報を基にグラフィックスの見栄えを良くしたり、ペアリングされたアクセサリやゲームコントローラを自動認識したり、プレイヤーのアクセシビリティ設定を反映したりします。また、ゲームがプラットフォームの最も一般的な操作方法に対応するようにしてください。ガイダンスは、[設定](/jp/design/human-interface-guidelines/settings)を参照してください。

**プレイを通じて教える。** ゲームの世界観の中で新しい情報やメカニクスを発見すると、プレイヤーの学習効果が高まる傾向があります。そのため、設定とオンボーディングのフローをプレイ可能なチュートリアルに組み込んで、プレイヤーを素早く引き込み、すぐに成功体験を得られるようにすると効果的です。書面のチュートリアルも用意する場合は、ゲームプレイの前提条件にするのではなく、分からないときに参照できるリソースとして提供することを検討してください。ガイダンスは、[オンボーディング](/jp/design/human-interface-guidelines/onboarding)を参照してください。

**リクエストは適切なタイミングまで先送りにする。** プレイの開始前にあまりに多くのリクエストを浴びせたくはありませんが、ゲームがAppleデバイスの特定のセンサーを使用したり、ハンドトラッキングのようにデータにアクセスすることでゲームプレイをパーソナライズしたりする場合は、最初にプレイヤーの許可を取る必要があります（ガイダンスは、[プライバシー](/jp/design/human-interface-guidelines/privacy)を参照してください）。そのようなリクエストを行う理由をユーザに理解してもらうために、データが必要になるシナリオに理由を組み込みます。例えば、最初のカットシーンから、プレイヤーが初めて手を使ってアクションを制御できるようになるまでの間に、プレイヤーの手をトラッキングする許可を取るとよいでしょう。また、ユーザが確実にゲームで充実した時間を過ごしたあとで、評価やレビューを求めるようにします（ガイダンスは、[評価とレビュー](/jp/design/human-interface-guidelines/ratings-and-reviews)を参照してください）。

[](/jp/design/human-interface-guidelines/launching)

[](/jp/design/human-interface-guidelines/onboarding)

[](/jp/design/human-interface-guidelines/loading)

## [どのディスプレイでも魅力的に見えるようにする](/jp/design/human-interface-guidelines/designing-for-games#Look-stunning-on-every-display)

**テキストは必ず判読可能にする。** ゲームのテキストが読みづらいと、プレイヤーが物語を追ったり、重要な指示や情報を理解したり、体験に集中したりするのに苦労することがあります。テキストを各デバイスで常に問題なく判読可能にするには、背景とはっきりと区別できるようにして、少なくともプラットフォームごとの推奨される最小テキストサイズを使用してください。ガイダンスは、[タイポグラフィ](/jp/design/human-interface-guidelines/typography)を参照してください。デベロッパ向けのガイダンスは、[ゲームのインターフェイスを小さい画面に適応させる](/documentation/Metal/adapting-your-game-interface-for-smaller-screens)（英語）を参照してください。

プラットフォーム| デフォルトのテキストサイズ| 最小テキストサイズ  
---|---|---  
iOS/iPadOS| 17 pt| 11 pt  
macOS| 13 pt| 10 pt  
tvOS| 29 pt| 23 pt  
visionOS| 17 pt| 12 pt  
watchOS| 16 pt| 12 pt  
  
**常に使いやすいボタンにする。** ボタンが小さすぎたり、ボタンどうしが互いに近すぎたりすると、プレイヤーはストレスを感じ、ゲームプレイの楽しさが低下します。各プラットフォームには、デフォルトの操作方法に基づいた推奨される最小ボタンサイズが定義されています。例えば、iOSのボタンは、タッチ操作ができるように最小でも44x44 ptとする必要があります。ガイダンスは、[ボタン](/jp/design/human-interface-guidelines/buttons)を参照してください。

プラットフォーム| デフォルトのボタンサイズ| 最小ボタンサイズ  
---|---|---  
iOS/iPadOS| 44x44 pt| 28x28 pt  
macOS| 28x28 pt| 20x20 pt  
tvOS| 66x66 pt| 56x56 pt  
visionOS| 60x60 pt| 28x28 pt  
watchOS| 44x44 pt| 28x28 pt  
  
**なるべく解像度に依存しないテクスチャやグラフィックスを使う。** 解像度に依存しないアセットを作成できない場合は、ゲームの解像度をデバイスの解像度に合わせます。visionOSでは、プレイヤーが見ている距離や角度に応じてシステムによって動的にサイズ調整されるため、常に見栄えがよいベクトルベースのアートが望ましいでしょう。ガイダンスは、[画像](/jp/design/human-interface-guidelines/images)を参照してください。

**レイアウトにデバイスの特徴を組み込む。** 例えば、デバイスの角が丸みをおびていたり、カメラハウジングがあったりする場合があり、これがインターフェイスの一部に影響することがあります。ゲームが各デバイスで自然に見えるようにするには、レイアウト中にそのような特徴を考慮し、可能な場合はプラットフォームで提供されるセーフエリアを利用してください（デベロッパ向けのガイダンスは、[セーフエリアと相対的にコンテンツを配置する](/documentation/UIKit/positioning-content-relative-to-the-safe-area)を参照してください）。ガイダンスは、[レイアウト](/jp/design/human-interface-guidelines/layout)を参照してください。セーフエリアガイドを含むテンプレートについては、[Appleデザインリソース](https://developer.apple.com/design/resources/)を参照してください。

**ゲーム内メニューはさまざまなアスペクト比に合うようにする。** ゲームはさまざまなアスペクト比（16:10、19.5:9、4:3など）で見栄えよく適切に動作する必要があります。特にゲーム内メニューは、ほかのコンテンツを見づらくすることなく、すべてのデバイスで判読可能かつ使いやすくする必要があります。また、対応している場合は、iPhoneとiPadの縦横両方の向きでもこれを考慮する必要があります。ゲーム内メニューが適切にレンダリングされるようにするには、相対的な制約に従ってさまざまなコンテキストに合うように調整される、動的なレイアウトの使用を検討してください。固定レイアウトはできる限り避け、デバイスに固有なカスタムのレイアウトを作成するのは必要な場合のみとしてください。ガイダンスは、[ゲーム内メニュー](/jp/design/human-interface-guidelines/menus#In-game-menus)を参照してください。

**フルスクリーン体験向けにデザインする。** 多くの場合、ユーザは、気を散らされないフルスクリーンでゲームプレイを楽しみます。macOS、iOS、およびiPadOSのフルスクリーンモードでは、ほかのアプリとシステムUIの一部を非表示にできます。visionOSでは、フルスペースで実行するゲームは完全にプレイヤーを囲んで、どこかほかの場所に移動したような感覚にすることができます。ガイダンスは、[フルスクリーンモード](/jp/design/human-interface-guidelines/going-full-screen)を参照してください。

[](/jp/design/human-interface-guidelines/layout)

[](/jp/design/human-interface-guidelines/typography)

[](/jp/design/human-interface-guidelines/going-full-screen)

## [直感的な操作を可能にする](/jp/design/human-interface-guidelines/designing-for-games#Enable-intuitive-interactions)

**各プラットフォームのデフォルトの操作方法に対応する。** 例えば、iPhoneでは通常、タッチを使ってゲームをプレイします。Macでは、プレイヤーはキーボードとマウスまたはトラックパッドの対応を想定する傾向があります。また、visionOSのゲームでは、間接的ジェスチャと直接的ジェスチャを行うときに目と手を使うことを想定しています。ゲームを各プラットフォームのデフォルトの操作方法に対応させるときには、コントロールのサイズとメニューの動作に特別な注意を払ってください。これは特に、ゲームをポインタベースのコンテキストからタッチベースにする場合に重要です。

プラットフォーム| デフォルトの操作方法| 追加の操作方法  
---|---|---  
iOS| タッチ| ゲームコントローラ  
iPadOS| タッチ| ゲームコントローラ、キーボード、マウス、トラックパッド、Apple Pencil  
macOS| キーボード、マウス、トラックパッド| ゲームコントローラ  
tvOS| リモコン| ゲームコントローラ、キーボード、マウス、トラックパッド  
visionOS| タッチ| ゲームコントローラ、キーボード、マウス、トラックパッド、空間ゲームコントローラ  
watchOS| タッチ| –  
  
**物理的なゲームコントローラに対応しながら、別の方法もユーザに提供する。** watchOS以外のすべてのプラットフォームが、物理的なゲームコントローラに対応しています。ゲームコントローラの存在は既存のゲームからの制御の移植や複雑な制御マッピングの処理を容易にしますが、すべてのプレイヤーが物理的なゲームコントローラを使用できるわけではないことを念頭に置いてください。できるだけ多くのプレイヤーがゲームを利用できるようにするには、ゲームの別の操作方法も提供してください。ガイダンスは[実物のゲームコントローラ](/jp/design/human-interface-guidelines/game-controls#Physical-controllers)を参照してください。

**iPhoneとiPadのタッチスクリーン体験を活用するタッチベースのゲームコントロールを提供する。** iOSとiPadOSでは、ゲームでプレイヤーがゲーム要素を直接操作したり、ゲームコンテンツに重なって表示される仮想コントロールを使用してゲームを操作したりすることができます。デザインのガイダンスは、[タッチコントロール](/jp/design/human-interface-guidelines/game-controls#Touch-controls)を参照してください。

[](/jp/design/human-interface-guidelines/game-controls)

[](/jp/design/human-interface-guidelines/gestures)

[](/jp/design/human-interface-guidelines/pointing-devices)

## [あらゆる人を迎え入れる](/jp/design/human-interface-guidelines/designing-for-games#Welcome-everyone)

**認識しやすさを優先する。** 視覚、聴覚、触覚のどれを使っていても、ユーザがゲームのコンテンツを確実に知覚できるようにします。例えば、カラーだけで重要な詳細を伝えたり、説明のサブタイトルが含まれていない、またはコンテンツを読むための別の方法を提供していないカットシーンを提供したりしないようにしましょう。具体的なガイダンスは、以下を参照してください:

  * テキストサイズ

  * カラーとエフェクト

  * モーション

  * 操作

  * ボタン

**プレイヤーが自分の体験をパーソナライズできるようにする。** プレイヤーによって好みや能力はさまざまで、ゲームの操作にも影響します。すべての人に合う万能な設定は存在しないため、プレイヤーが文字サイズ、ゲーム制御マッピング、モーションの強さ、サウンドバランスなどのパラメータをカスタマイズできるようにします。システムフレームワークと[Unityプラグイン](https://github.com/Apple/UnityPlugins)のいずれを使用している場合も、内蔵の[Appleアクセシビリティ技術](https://developer.apple.com/accessibility/)を活用して、アクセシビリティのパーソナライズに対応することができます。

**プレイヤーが自分を表現するために必要なツールを提供する。** プレイヤーにアバターを作成したり名前や説明を提供するように勧めるゲームの場合は、幅広い自己認識に対応し、できるだけ多くの人間の特徴を表現するオプションを提供してください。

**ストーリーやキャラクターに対するステレオタイプを避ける。** ゲームのキャラクターやシナリオを、現実世界の固定観念を残すような方法で描写していないかどうか、自問してください。例えば、敵を、特定の人種、性別、または文化遺産として描写していないでしょうか? ゲームを見直して偏見や固定観念を見つけて取り除き、現実世界の文化や言語の参照が必要な場合は、必ず敬意を払ってください。

[](/jp/design/human-interface-guidelines/accessibility)

[](/jp/design/human-interface-guidelines/inclusion)

## [Appleのテクノロジーを採用する](/jp/design/human-interface-guidelines/designing-for-games#Adopt-Apple-technologies)

**Game Centerを組み込んでプレイヤーがどのデバイスでもゲームを見つけて友達とつながれるようにする。** [Game Center](https://developer.apple.com/game-center/)はすべてのプラットフォームで使用できるAppleのソーシャルゲームネットワークです。Game Centerを使用すると、プレイヤーは自分の達成状況や達成項目をトラッキングしたり、ゲーム内でLeaderboard、チャレンジ、マルチプレイヤーアクティビティを設定したりできます。デザインのガイダンスは[Game Center](/jp/design/human-interface-guidelines/game-center)を、デベロッパ向けのガイダンスは[GameKit](/documentation/GameKit)を参照してください。

**プレイヤーがどのデバイスでもゲームを再開できるようにする。** 多くの場合、プレイヤーは複数のAppleデバイスで1つのiCloudアカウントを使用しています。[GameSave](/documentation/GameSave)に対応すると、プレイヤーがゲームの状態を保存して、まさに中断した場所から別のデバイスで再開することができます。

**触覚フィードバックに対応してプレイヤーがアクションを体感できるようにする。** Core Hapticsを使用すると、カスタムの触覚パターンを作成して提供できるようになり、カスタムのオーディオコンテンツと組み合わせることもできます。Core HapticsはiOS、iPadOS、tvOS、およびvisionOSで使用可能で、多くのゲームコントローラが対応しています。ガイダンスは[触覚フィードバックの提供](/jp/design/human-interface-guidelines/playing-haptics)を参照してください。デベロッパ向けのガイダンスは[Core Haptics](/documentation/CoreHaptics)および[ゲームコントローラでの触覚フィードバックの提供](/documentation/CoreHaptics/playing-haptics-on-game-controllers)を参照してください。

**空間オーディオを使ってプレイヤーをゲームのサウンドスケープに没入させる。** マルチチャンネルオーディオを提供することで、ゲームのオーディオを自動的に現在のデバイスに適応させて、対応している場合はイマーシブな空間オーディオ体験を可能にすることができます。ガイダンスは[オーディオの再生＞visionOS](/jp/design/human-interface-guidelines/playing-audio#visionOS)を参照してください。デベロッパ向けのガイダンスは[空間オーディオの可能性を探る](https://developer.apple.com/news/?id=fakg1z5b)を参照してください。

**Appleの技術を活用してユニークなゲームプレイのメカニクスを可能にする。** 例えば、拡張現実、機械学習、[HealthKit](/documentation/HealthKit)などの技術を組み込んだり、位置情報データおよびカメラやマイクといった機能へのアクセスをリクエストしたりできます。Appleのテクノロジー、機能、およびサービスの完全なリストについては、[テクノロジー](/jp/design/human-interface-guidelines/technologies)を参照してください。

[](/jp/design/human-interface-guidelines/game-center)

[](/jp/design/human-interface-guidelines/icloud)

[](/jp/design/human-interface-guidelines/in-app-purchase)

## [リソース](/jp/design/human-interface-guidelines/designing-for-games#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/designing-for-games#Related)

[Game Center](/jp/design/human-interface-guidelines/game-center)

[ゲームコントロール](/jp/design/human-interface-guidelines/game-controls)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/designing-for-games#Developer-documentation)

[Games Pathway](https://developer.apple.com/games/get-started/)

[Appleプラットフォーム向けのゲームを作成する](https://developer.apple.com/games/)

#### [ビデオ](/jp/design/human-interface-guidelines/designing-for-games#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/209)

[](https://developer.apple.com/videos/play/wwdc2024/10085)

## [変更履歴](/jp/design/human-interface-guidelines/designing-for-games#Change-log)

日付| 変更内容  
---|---  
2025年6月09日| タッチベースのコントロールとGame Centerに関するガイダンスを更新。  
2024年6月10日| 新規ページ。
