# Game Center

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/game-center

# Game Center

Game Centerは、Appleのソーシャルゲームネットワークです。プレイヤーは達成状況をトラッキングしたり、Appleのプラットフォーム上で友達とつながったりできます。また、プレイヤー同士のデバイスでゲームが見つかりやすくなります。

![Game Centerアイコンのスケッチ。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる青色になっています。](https://docs-assets.developer.apple.com/published/4df10f335123d3744626913e7fc71a02/technologies-Game-Center-intro%402x.png)

Game Center対応のゲームにすると、プレイヤーは以下を行えるようになります。

  * 友達がプレイしている新しいゲームを発見する。

  * 友達をスムーズにゲームに招待する。

  * Apple Gamesアプリ、App Store、通知など、システム全体で最新のゲームアクティビティを確認する。

Game Centerに対応すると、このようなプレイヤーアクティビティが可能になるので、ゲームがAppleのプラットフォーム上で見つかりやすくなります。

ゲームにGame Centerを組み込むには、GameKitフレームワークを使います。このフレームワークではフル機能のUIが提供されており、プレイヤーはゲーム内で簡単にGame Centerデータにアクセスして表示できるようになります。また、GameKitを使ってこのデータを独自のカスタムUI内に表示させることも可能です。デベロッパ向けのガイダンスは、[GameKit](/documentation/GameKit)を参照してください。

## [Game Centerにアクセスする](/jp/design/human-interface-guidelines/game-center#Accessing-Game-Center)

プレイヤーに最高のGame Center体験を提供するには、まず、ゲームの起動時にプレイヤーがシステム上でGame Centerアカウントにサインインしているか確認します。サインインしていない場合は、その段階でGame Centerにサインインしてもらいます。こうすることで非常にシームレスなユーザ体験になり、「トッププレイ」チャートやプレイヤーの友達からのおすすめなどを通じたゲームの見つかりやすさが最も高くなります。

### [アクセスポイントを組み込む](/jp/design/human-interface-guidelines/game-center#Integrating-the-access-point)

Game Centerの _アクセスポイント_ は、ゲームを離れることなくGame Centerのプロフィールや情報を確認できるAppleによってデザインされたUI要素です。デベロッパ向けのガイダンスは、[ゲームにアクセスポイントを追加する](/documentation/GameKit/adding-an-access-point-to-your-game)を参照してください。

![The Coastというゲームのタイトル画面が表示されているiPhoneのスクリーンショット。斜めになったロケットのシンボルが入った円形のボタンで示されているアクセスポイントコントロールが、先頭側上部の隅にあります。](https://docs-assets.developer.apple.com/published/004448a72914f3893a19bdedeb1c5b39/games-access-point-collapsed%402x.png)

iOS、iPadOS、macOSでは、アクセスポイントからゲームオーバーレイにアクセスできます。これはシステム上のオーバーレイで、プレイヤーは達成状況を確認したり、ゲームアクティビティを開始したりできます。

![iPhoneのスクリーンショットとiPadのスクリーンショットで構成された図。どちらの画面もThe Coastというゲームの画面で、上部にゲームオーバーレイが表示されています。iPhoneのスクリーンショットではオーバーレイが画面全体を覆っていますが、iPadのスクリーンショットでは、オーバーレイは末尾側に縦に表示されています。](https://docs-assets.developer.apple.com/published/d45bb0d73f7fb9c7d3ccae51fccd57e0/games-game-overlay%402x.png)

visionOSとtvOSでは、アクセスポイントからゲーム内ダッシュボードにアクセスできます。これは、プレイヤーのGame Centerアクティビティにアクセスできるフルスクリーンのビューで、ゲーム画面に重ねて表示されます。

**メニュー画面にアクセスポイントを表示する。** アクセスポイントは、ゲームのメインメニューか設定領域に追加するようにしましょう。プレイ中の画面や一時的なスプラッシュ画面、シネマティックフロー、メインメニュー画面の前に表示されるチュートリアルにアクセスポイントを表示するのは避けてください。

**アクセスポイントの近くにコントロールを置かない。** アクセスポイントは、画面の四隅いずれかの位置に固定表示できます。アクセスポイントには縮小版と拡大版の両方があるため、アクセスポイントが重要なUIやコントロールに重ならないか確認し、必要に応じてレイアウトを調整してください。

注意

visionOSでは、アクセスポイントの位置はゲームの種類（イマーシブやボリュームベースなど）によって異なります。デベロッパ向けのガイダンスは、[ゲームにアクセスポイントを追加する](/documentation/GameKit/adding-an-access-point-to-your-game#Configure-the-access-point-on-visionOS)を参照してください。

**ゲームオーバーレイやダッシュボードの表示中はゲームを一時停止することを検討する。** ゲームを一時停止させると、プレイヤーがゲームの進行を心配せずにGame Centerの情報を確認できるようになります。

### [カスタムUIを使用する](/jp/design/human-interface-guidelines/game-center#Using-custom-UI)

ゲームには、ゲームオーバーレイ（iOS、iPadOS、macOSの場合）またはダッシュボード（visionOS、tvOSの場合）へのカスタムリンクを含めることができます。カスタムUIでは、どちらの場合でも、LeaderboardやプレイヤーのGame Centerプロフィールといった特定の領域にディープリンクさせることができます。

**Game Centerで提供されているアートワークをカスタムリンクで使用する。** カスタムUIでGame Center機能を参照する場合は、[Appleのデザインリソース](https://developer.apple.com/design/resources/#technologies)にある公式のアートワークを使用します。公式アートワークの見た目は維持し、寸法や視覚効果を変更しないでください。

**カスタムリンクでは正しい用語を使用する。** カスタムUIでプレイヤーが戸惑わないように、Game Center用語を正しく使用する方法については、以下の表を参考にしてください。

正しい用語| 正しくない用語| 訳語  
---|---|---  
Game Center| GameKit、GameCenter、game center|  _Game Center_ にはシステムの公式の訳語を当てる  
Game Centerプロフィール| プロフィール、アカウント、プレイヤー情報|  _Game Center_ にはシステムの公式の訳語を当て、 _Profile_ は翻訳する  
達成項目| 報酬、トロフィー、メダル|   
Leaderboard| ランキング、スコア、リーダー|   
チャレンジ| 競争|   
友達を追加| 追加、プロフィールを追加、フレンドを含める|   
  
## [達成項目](/jp/design/human-interface-guidelines/game-center#Achievements)

達成項目は、ゲームをプレイし続けたいというプレイヤーの意欲を高める仕掛けです。Game Centerの達成項目はトレーディングカード風に表示され、プレイヤーの進行状況や独自の画像を見せることができるようになっています。デベロッパ向けのガイダンスは、[達成項目でプレイヤーに達成感を与える](/documentation/GameKit/rewarding-players-with-achievements)を参照してください。

![The Coastというゲームが表示されているiPhoneのスクリーンショット。ゲームオーバーレイが開き、達成項目の概要画面が表示されています。](https://docs-assets.developer.apple.com/published/52e3db014d3522805c8390e55abddff3/games-achievement-overlay%402x.png)

達成項目の概要

![The Coastというゲームが表示されているiPhoneのスクリーンショット。ゲームオーバーレイが開き、特定の達成項目の詳細が表示されています。](https://docs-assets.developer.apple.com/published/3f23f01922c111472fabe0abb0aa3a5f/games-achievement-overlay-detail%402x.png)

達成項目の詳細

### [達成項目をゲームに組み込む](/jp/design/human-interface-guidelines/game-center#Integrating-achievements-into-your-game)

**Game Centerの達成項目の状態を一致させる。** Game Centerでは、達成項目の状態が4種類定義されています（ロック中（locked）、進行中（in-progress）、非表示（hidden）、完了（completed））。達成項目は完了のステータスごとに自動的にグループ化され、完了した達成項目は「完了」グループに、それ以外の達成項目はすべて「ロック中」グループに表示されます。ゲーム内の達成項目を、Game Centerの達成項目に定義されている4種類の状態に合わせれば、プレイヤー体験に一貫性を持たせ、一目見ただけで達成項目の種類が分かるようにすることができます。

**表示順を決める。** 達成項目はアップロードされた順に表示されるため、ファイルをアップロードする前に表示順を検討してください。例えば、達成項目を、ゲームの最も一般的な進め方と一致する順に表示するのも1つの方法です。

**達成項目の説明は簡潔にする。** 達成項目カードのタイトルと説明には行数制限（2行）があります。タイトルや説明が折り返されて2行を超えた場合、以降のテキストは表示されません。達成項目のタイトルではタイトルスタイルの大文字化（英語の場合）を、説明ではセンテンススタイルの大文字化を使用してください。

![達成項目カードの図。達成項目画像、タイトル、説明を示すコールアウトが付いています。](https://docs-assets.developer.apple.com/published/25e942df81ccd2083613c202637a020d/games-achievement-anatomy%402x.png)

**プレイヤーに達成状況を伝える。** 段階的な達成項目にすると、プレイヤーの進行状況が表示され、「The Coastの『五大湖の貨物船』はもう半分以上進んでいます。この調子で頑張りましょう!」のような励ましのメッセージを提供して、最後まで達成するようプレイヤーのモチベーションを高めることができます。

### [達成項目画像を作成する](/jp/design/human-interface-guidelines/game-center#Creating-achievement-images)

**プレイヤーに達成感を与える豪華な高品質画像をデザインする。** 達成項目はGame Center UIの中でも目立つ要素なので、プレイヤーの目を引きゲームに戻りたいと思わせるような、見栄えのする高品質のアセットをデザインすることが重要です。複数の達成項目で同じ画像を使い回すのは避けましょう。達成項目画像を用意しなかった場合、カードには代わりにプレースホルダ画像が表示されます。

**アートワークを適切なサイズとフォーマットで作成する。** 達成項目画像は円形にマスキングされるため、重要な部分が中央に来るようにしましょう。画像を作成するときは以下の仕様に従ってください。

![iOS、iPadOS、macOS、visionOSでの達成項目画像のレイアウト図。画像サイズとマスクの直径を示すコールアウトが付いています。](https://docs-assets.developer.apple.com/published/4915c4afac49676ef39b7f2c1dc3f6c5/ios-achievement-image-layout%402x.png)

属性| 値  
---|---  
フォーマット| PNG、TIF、またはJPG  
色空間| sRGBまたはP3  
解像度| 72 DPI（最小）  
画像サイズ| 512x512 pt（1024x1024 px @2x）  
マスクの直径| 512 pt（1024 px @2x）  
  
![tvOSでの達成項目画像のレイアウト図。画像サイズとマスクの直径を示すコールアウトが付いています。](https://docs-assets.developer.apple.com/published/b506be028bdd74b97ec06e85d2669684/tvos-achievement-image-layout%402x.png)

属性| 値  
---|---  
フォーマット| PNG、TIF、またはJPG  
色空間| sRGBまたはP3  
解像度| 72 DPI（最小）  
画像サイズ| 320x320 pt（640x640 px @2x）  
マスクの直径| 200 pt（400 px @2x）  
  
## [Leaderboard](/jp/design/human-interface-guidelines/game-center#Leaderboards)

Leaderboardは、ゲーム内でのフレンドリーな競争を促すのに非常に効果的です。Game Centerに対応すると、プレイヤーは友達内や全世界でのランクを簡単にチェックできるほか、友達から挑戦を受けたときや、Leaderboardで自分のスコアが友達に抜かれたときに通知を受けることができます。Leaderboard情報を表示するには、システムが提供するUIまたはカスタムのUIを使用します。デベロッパ向けのガイダンスは、[Leaderboardで進行と競争を促す](/documentation/GameKit/encourage-progress-and-competition-with-leaderboards)を参照してください。

![The Coastというゲームが表示されているiPhoneのスクリーンショット。ゲームオーバーレイが開き、Leaderboardの概要画面が表示されています。](https://docs-assets.developer.apple.com/published/82e52c3c4e84fd860b1dff8565f7c51d/games-leaderboards-overlay%402x.png)

Leaderboardの概要

![The Coastというゲームが表示されているiPhoneのスクリーンショット。ゲームオーバーレイが開き、特定のLeaderboardの詳細が表示されています。](https://docs-assets.developer.apple.com/published/ad8fe7a04fd16a3913719dff0ccc3d66/games-leaderboards-detail%402x.png)

Leaderboardの詳細

**Leaderboardの種類を選ぶ。** Game Centerは、 _クラシック_ と _定期更新型_ という、2種類のLeaderboardに対応しています。

  *  _クラシックなLeaderboard_ は、プレイヤーの歴代最高スコアを記録します。クラシックなLeaderboardは常にアクティブで、終了期限はありません。クラシックなLeaderboardには、次のようなゴールを設定できます。

    * リズムゲームで最高スコアを出す。

    * 1回のダンジョン探索で最多コインを収集する。

    * エンドレスモードで最長連続プレイ時間を達成する。

  *  _定期更新型のLeaderboard_ は、定義したインターバル（毎週、毎日など）でリセットされます。定期更新型のLeaderboardなら誰にでもトップに立つチャンスが生まれるため、参加意欲を高めることができます。定期更新型のLeaderboardは、次のような特徴を持つゲームに最適です。

    * 日替わりパズル

    * 季節や祝日がテーマのイベント

    * バトルモードごとの週間ランキングのLeaderboard

**複数のLeaderboardでLeaderboardセットを利用する。** Leaderboardセットは、Leaderboardを見つけやすくするためにLeaderboardをまとめる仕組みです。Leaderboardを、次のようなテーマやプレイ体験ごとにまとめることを検討してください。

  * 難易度（イージー、ノーマル、ハード）

  * アクティビティの種類（戦闘、クラフト、収集）

  * ジャンルやテーマ（ディスコ、ポップ、ロック）

**Leaderboard画像を追加する。** Leaderboardアートワークを追加すると、ゲームのビジュアルデザインをさらに充実させることができます。ひとつひとつのLeaderboardに、Leaderboardのランク付けに関わるゲームプレイを反映し、それを魅力的に伝える専用の画像を作成することを目指しましょう。Leaderboardはシステム全体に表示され、プレイヤーが友達と交流し、競争するよう促す役割を果たします。魅力的な画像を設定することで、プレイヤーを引きつけて、ゲーム体験の雰囲気を伝えることができます。

iOS、iPadOS、macOS向けのゲームでは、Leaderboard画像に1つの画像を使用します。tvOS向けゲームの場合は、アートワークにフォーカスした際にアニメーション表示されるように一式の画像を用意してください。フォーカスエフェクトについて詳しくは、[フォーカスと選択](/jp/design/human-interface-guidelines/focus-and-selection)を参照してください。フォーカス可能な画像の作成についてのヘルプが必要な場合は、[Appleのデザインリソース](https://developer.apple.com/design/resources/#tvos-apps)でtvOSのテンプレートをダウンロードしてください。Leaderboardアートワークを作成するときは以下の仕様に従ってください。

![iOS、iPadOS、macOSでのLeaderboard画像のレイアウト図。画像サイズとマスクの直径を示すコールアウトが付いています。](https://docs-assets.developer.apple.com/published/fc30a7027550a0ca4b32c301c2178d48/leaderboard-image-layout-general%402x.png)

属性| 値  
---|---  
フォーマット| JPEG、JPG、またはPNG  
色空間| sRGBまたはP3  
解像度| 72 DPI（最小）  
画像サイズ| 512x512 pt（1024x1024 px @2x）  
切り取り後の領域| 512x312 pt（1024x624 px @2x）  
  
![tvOSでのLeaderboard画像のレイアウト図。画像サイズ、フォーカスされているときのサイズ、フォーカスされていないときのサイズを示すコールアウトが付いています。](https://docs-assets.developer.apple.com/published/a20d418a850463ce0706ff5c0ea845f6/tvos-multi-layered-leaderboard-image%402x.png)

属性| 値  
---|---  
フォーマット| PNG、TIF、またはJPG  
色空間| sRGBまたはP3  
解像度| 72 DPI（最小）  
画像サイズ| 659x371 pt（1318x742 px @2x）  
フォーカスされているとき| 618x348 pt（1236x696 px @2x）  
フォーカスされていないとき| 548x309 pt（1096x618 px @2x）  
  
注意

切り取りがLeaderboardアートワークに与える影響については注意してください。iOS、iPadOS、macOSでは、Leaderboardセットに含まれているLeaderboardのアートワークが切り取られます。tvOSでは、Leaderboardアートワークでのフォーカスエフェクトによって、画像の一部のレイヤーの端が切り取られることがあります。どちらの場合でも、メインの部分が余裕をもって表示領域に収まるようにしましょう。

## [チャレンジ](/jp/design/human-interface-guidelines/game-center#Challenges)

チャレンジは、シングルプレイヤーのアクティビティを、友達とのマルチプレイヤー体験に変える仕組みです。チャレンジはLeaderboardを基盤に構築されており、プレイヤーは友達とつながって、制限時間付きの競争に参加できます。デベロッパ向けのドキュメントは、[Leaderboardから魅力的なチャレンジを作成する](/documentation/GameKit/creating-engaging-challenges-from-leaderboards)を参照してください。

![The Coastというゲームが表示されているiPhoneのスクリーンショット。ゲームオーバーレイが開き、チャレンジの概要画面が表示されています。](https://docs-assets.developer.apple.com/published/b27249dbd318a50ba47bfe2329f8124d/games-challenges-overlay%402x.png)

チャレンジの概要

![The Coastというゲームが表示されているiPhoneのスクリーンショット。ゲームオーバーレイが開き、特定のチャレンジの詳細が表示されています。](https://docs-assets.developer.apple.com/published/6f6cb506dfe3baa90098fe787b7e014d/games-challenges-overlay-detail%402x.png)

チャレンジの詳細

**魅力的なチャレンジを作成する。** チャレンジは、プレイヤーの達成度を明確に評価できる、短時間のスキルベースのゲームプレイアクティビティに最適です。プレイヤーが単独でプレイでき、1～5分で完了できるチャレンジを作成しましょう。魅力的なチャレンジには、次のようなものが含まれます。

  * レースステージで最速ラップタイムを記録する。

  * 1ラウンドで最も多くの敵を倒す。

  * 日替わりパズルを最小限のミスで解く。

**全体的な達成状況や個人のベストスコアを記録するチャレンジは作成しないようにする。** 定期的にプレイしているプレイヤーが有利になり、不公平感が生まれる可能性があります。その代わりに、プレイヤーがチャレンジに挑戦するたびに最新のスコアを記録しましょう。こうすると、すべてのプレイヤーが同じ条件で競えるようになり、チャレンジへの参加意欲が保たれやすくなります。

**簡単にチャレンジに参加できるようにする。** プレイヤーは、招待リンク、ゲームオーバーレイ、またはiOS、iPadOS、macOSのGamesアプリからチャレンジにアクセスできます。必ずチャレンジが開始されるモードまたはレベルに直接ディープリンクさせ、初めて参加するプレイヤーがチャレンジ開始前に必要な初期オンボーディングを完了できるようにしてください。例えば、ゲームの基本操作を理解するためにチュートリアルレベルが必要な場合は、最初にチュートリアルに遷移させ、あとでチャレンジが自動的に開始されることをUIに表示して伝えましょう。

![チャレンジカードの図。チャレンジのタイトル、アートワーク、プレイヤー数、およびシステムが提供するカード下部のグラデーションを示すコールアウトが付いています。](https://docs-assets.developer.apple.com/published/072ab95bec4bb6c51380ed06099adb6f/games-challenge-anatomy%402x.png)

**プレイヤーにチャレンジへの参加を促す高品質のアートワークを作成する。** チャレンジのアートワークは、ゲームオーバーレイ、Gamesアプリ、招待リンクのプレビューに表示されます。アートワーク内の主要なコンテンツを、チャレンジのタイトルや説明が重なってしまう可能性がある領域に配置しないようにしてください。チャレンジ画像内でテキストを使う必要がある場合は、App Store ConnectまたはXcodeで適切なローカライズ版を提供してください。チャレンジのアートワークを作成するときは以下の仕様に従ってください。

![チャレンジ画像のレイアウト図。画像サイズと切り取り後の領域を示すコールアウトが付いています。](https://docs-assets.developer.apple.com/published/27850c347e484601bf78a28f81a31497/games-challenge-image-specs%402x.png)

属性| 値  
---|---  
フォーマット| JPEG、JPG、またはPNG  
色空間| sRGBまたはP3  
解像度| 72 DPI（最小）  
画像サイズ| 1920x1080 pt（3840x2160 px @2x）  
切り取り後の領域| 1465x767 pt（2930x1534 px @2x）  
  
## [マルチプレイヤーアクティビティ](/jp/design/human-interface-guidelines/game-center#Multiplayer-activities)

Game Centerはリアルタイムとターン形式の両方のマルチプレイヤーアクティビティに対応しており、友達やほかのプレイヤーと簡単につながることができます。プレイヤーは、パーティーコード、ゲームオーバーレイ、ダッシュボード、Gamesアプリからマルチプレイヤーのゲームプレイにアクセスできます。デベロッパ向けのドキュメントは、[ゲーム用のアクティビティを作成する](/documentation/GameKit/creating-activities-for-your-game)を参照してください。

![The Coastというゲームが表示されているiPhoneのスクリーンショット。ゲームオーバーレイが開き、マルチプレイヤーレベルの概要画面が表示されています。](https://docs-assets.developer.apple.com/published/8a4a58e6875c3547929283017e210aa9/games-multiplayer-overlay%402x.png)

マルチプレイヤーレベルの概要

![The Coastというゲームが表示されているiPhoneのスクリーンショット。ゲームオーバーレイが開き、特定のマルチプレイヤーレベルの詳細が表示されています。](https://docs-assets.developer.apple.com/published/1e98bddc2856b36087ed5b33c137e956/games-multiplayer-overlay-detail%402x.png)

マルチプレイヤーレベルの詳細

**パーティーコードを使ってプレイヤーをマルチプレイヤーアクティビティに招待する。** Game Centerのパーティーコードは、リアルタイムのマルチプレイヤーセッションをスムーズに実現するのに最適な方法です。パーティーコードは、Game Centerのマッチメイキングとネットワーク機能を使う場合でも、独自の方法を提供する場合でも使えます。パーティーコードはGame Centerによって生成され、通常は8文字の英数字（例: 「2MP4-9CMF」）になります。 パーティーコードをマルチプレイヤーゲームに組み込む場合は、最高のプレイヤー体験を提供するため、以下のガイドラインを参考にしてください。

  * プレイヤーがゲームプレイに途中参加、途中離脱、再参加できるようにする。

  * プレイヤーがゲーム内で現在のパーティーコードを表示できる方法を提供する。

  * プレイヤーがパーティーコードを手動入力できるようにする。

![The Coastというゲームが表示されているiPhoneのスクリーンショット。ゲームオーバーレイが開き、カスタムコードを使ってマルチプレイヤーアクティビティに参加したり設定したりするゲーム内UIが表示されています。](https://docs-assets.developer.apple.com/published/06bcea97f97c8315531c845ede2d5e87/games-multiplayer-custom-code%402x.png)

**ゲーム内UIを通じてマルチプレイヤーアクティビティに対応する。** ゲームオーバーレイとGame Centerのダッシュボードを使うと、プレイヤーがゲームを離れずにマルチプレイの対戦相手を見つけられるようになります。Game Centerのデフォルトのマルチプレイヤー用インターフェイスでは、近くのプレイヤー、最近対戦したプレイヤー、Game Centerの友達、連絡先の人を招待できます。また、カスタムUI内にマルチプレイヤー機能を表示させることも可能です。デベロッパ向けのガイダンスは、[ゲームで複数のプレイヤーを見つける](/documentation/GameKit/finding-multiple-players-for-a-game)を参照してください。

![The Coastというゲームが表示されているiPhoneのスクリーンショット。ゲームオーバーレイが開き、マルチプレイヤーアクティビティを開始するゲーム内UIが表示されています。](https://docs-assets.developer.apple.com/published/132e90bce634e08ff839c02a4ff443ca/games-multiplayer-in-game-ui%402x.png)

**魅力的なアクティビティアートワークを用意する。** パーティーコード、Gamesアプリ、ゲーム内UIなど、プレイヤーはシステム全体でマルチプレイヤーアクティビティのプレビュー画像を目にすることになります。アートワークを作成するときは以下の仕様に従ってください。

![マルチプレイヤーアクティビティカードの図。アクティビティのタイトル、アートワーク、プレイヤー数、およびシステムが提供するカード下部のグラデーションを示すコールアウトが付いています。](https://docs-assets.developer.apple.com/published/16dfb55c7611b33859066ccdcc87d5e5/games-multiplayer-anatomy%402x.png)

![マルチプレイヤーアクティビティ画像のレイアウト図。画像サイズと切り取り後の領域を示すコールアウトが付いています。](https://docs-assets.developer.apple.com/published/27850c347e484601bf78a28f81a31497/games-multiplayer-image-specs%402x.png)

属性| 値  
---|---  
フォーマット| JPEG、JPG、またはPNG  
色空間| sRGBまたはP3  
解像度| 72 DPI（最小）  
画像サイズ| 1920x1080 pt（3840x2160 px @2x）  
切り取り後の領域| 1465x767 pt（2930x1534 px @2x）  
  
## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/game-center#Platform-considerations)

 _iOS、iPadOS、macOS、visionOSに追加の考慮事項はありません。_

### [tvOS](/jp/design/human-interface-guidelines/game-center#tvOS)

**ダッシュボードの上部に任意で画像を表示する。** tvOSでは、ダッシュボードに追加のアートワークを表示して、ゲームのデザインを強調することができます。遠くからでも見栄えがして認識しやすいシンプルな画像を使用しましょう。ゲームのロゴやワードマークの使用を検討してください。ただし、この画像にアプリのアイコンを使用しないでください。ダッシュボード画像を作成するときは以下の仕様に従ってください。

![tvOSのダッシュボード画像のレイアウト図。画像サイズを示すコールアウトが付いています。](https://docs-assets.developer.apple.com/published/438f3caaa842926ba5a0f54470c64373/tvos-dashboard-image%402x.png)

属性| 値  
---|---  
画像サイズ| 600x180 pt（1200x360 px @2x）  
フォーマット| PNG、TIF、またはJPG  
色空間| sRGBまたはP3  
解像度| 72 DPI（最小）  
  
### [watchOS](/jp/design/human-interface-guidelines/game-center#watchOS)

**watchOSでのGame Center対応には注意する。** GameKitの機能とAPIはwatchOSゲームでも利用できますが、watchOS上で呼び出せるGame CenterのシステムUIは用意されていません。代わりに、watchOSゲーム向けのGame Centerコンテンツは、接続されているiPhoneに表示されます。

## [リソース](/jp/design/human-interface-guidelines/game-center#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/game-center#Related)

[ゲーム向けのデザイン](/jp/design/human-interface-guidelines/designing-for-games)

[ゲームコントロール](/jp/design/human-interface-guidelines/game-controls)

[Appleデザインリソース](https://developer.apple.com/design/resources/#technologies)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/game-center#Developer-documentation)

[GameKit](/documentation/GameKit)

[ゲーム用のアクティビティを作成する](/documentation/GameKit/creating-activities-for-your-game)

[Leaderboardから魅力的なチャレンジを作成する](/documentation/GameKit/creating-engaging-challenges-from-leaderboards)

[Appleプラットフォーム向けのゲームを作成する](https://developer.apple.com/games/)

[Game Porting Toolkit](https://developer.apple.com/games/game-porting-toolkit/)

#### [ビデオ](/jp/design/human-interface-guidelines/game-center#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/214)

[](https://developer.apple.com/videos/play/wwdc2025/215)

## [変更履歴](/jp/design/human-interface-guidelines/game-center#Change-log)

日付| 変更内容  
---|---  
2025年6月09日| 新しいチャレンジとマルチプレイヤーアクティビティのガイダンス、Apple Gamesアプリとゲームオーバーレイの考慮事項を追加。アクティビティのプレビュー画像のガイダンスと仕様を更新。  
2024年2月02日| visionOSのゲームでのアクセスポイントとダッシュボードの使用に関するデベロッパ向けのガイダンスのリンクを追加。  
2023年9月12日| iOSの達成項目レイアウトのアートワークを追加。  
2023年5月02日| ガイダンスを1ページに統合しました。
