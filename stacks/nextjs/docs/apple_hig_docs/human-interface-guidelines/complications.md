# コンプリケーション

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/complications

# コンプリケーション

コンプリケーションは、ユーザが手首を上げてApple Watchを見るたびに、文字盤に最新の関連情報を表示する機能です。

![図案化されたApple Watchの文字盤。時刻と、ラベルの付いたさまざまなサイズのコンプリケーションがあります。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/c93c58345d92cef3477cdf2cf3b008c4/components-complications-intro%402x.png)

気になっているデータをアプリを開かずに素早く確認できるので、強力なコンプリケーションを複数提供するアプリは多くのユーザに好評です。

ほとんどの文字盤には少なくとも1つのコンプリケーションが表示されます。4つ以上のコンプリケーションを表示できる場合もあります。

watchOS 9以降では、コンプリケーション（ _アクセサリ_ とも呼ばれる）が[円形](https://developer.apple.com/jp/design/human-interface-guidelines/complications#Circular)や[インライン](https://developer.apple.com/jp/design/human-interface-guidelines/complications#Inline)などいくつかのファミリーに分類され、アプリのコンプリケーションデータの表示に使える推奨レイアウトが定義されています。文字盤のコンプリケーションスロットごとに表示できるファミリーを指定できます。古いバージョンのwatchOSで動作するコンプリケーションでは[レガシーテンプレート](https://developer.apple.com/jp/design/human-interface-guidelines/complications#Legacy-templates)を使えます。それらのテンプレートでは、ユーザが選択した色を反映しない非グラフィックのコンプリケーションスタイルが定義されます。

デベロッパ向けメモ

watchOS 9以降のコンプリケーションの開発では、なるべく[WidgetKit](/documentation/WidgetKit)を使用してください。ガイダンスは、[ClockKitのコンプリケーションをWidgetKitに移行する方法](/documentation/WidgetKit/Converting-A-ClockKit-App)を参照してください。古いバージョンのwatchOSに対応する場合は、引き続きClockKitコンプリケーションデータソースプロトコルを実装してください（[`CLKComplicationDataSource`](/documentation/ClockKit/CLKComplicationDataSource)を参照）。

## [ベストプラクティス](/jp/design/human-interface-guidelines/complications#Best-practices)

**ユーザが一目で確認する必要がある、不可欠で動的なコンテンツを見極める。** アプリを素早く起動できるのもコンプリケーションの便利な機能ですが、ユーザがさらに高く評価するのは、重要な情報をいつも最新の状態で把握できるようにする機能です。最新の有意義なデータを表示しない静的なコンプリケーションは、文字盤の目立つ場所への配置を維持することが難しくなります。

**可能な限りすべてのコンプリケーションファミリーに対応する。** 対応するファミリーを増やすと、アプリのコンプリケーションが文字盤に表示される可能性が高まります。特定のコンプリケーションファミリーで役立つ情報をどうしても表示できない場合は、少なくともユーザが文字盤からアプリを起動できるように、アプリアイコンなどの画像を提供してください。

**ファミリーごとに複数のコンプリケーションを作成することを検討する。** 複数のコンプリケーションに対応すると、共有可能な文字盤を利用することができます。ユーザはそこから、愛用のアプリ1つに特化した文字盤を構成できます。例えば、トライアスロンのトレーニング用アプリで種目ごとに1つ、全部で3つの円形コンプリケーションを作成し、各コンプリケーションからアプリ内の種目専用領域にディープリンクするように設計できます。カスタムの画像や色を使って水泳、自転車、長距離走のコンプリケーションを同時に表示するように構成された、共有可能な文字盤を提供するのもよい考えです。ユーザはこの文字盤を選択することで、設定を何も行わずに文字盤の利用を開始できます。ガイダンスは[文字盤](/jp/design/human-interface-guidelines/watch-faces)を参照してください。

**対応するコンプリケーションごとに異なるディープリンクを定義する。** コンプリケーションごとに最も関連性の高いアプリ内の領域が開くようにすると、アプリの使い勝手が向上します。提供するすべてのコンプリケーションからアプリ内の同一の箇所が開くと、使い勝手が悪いという印象を与えかねません。

**常にプライバシーに配慮する。** 常時表示のRetinaディスプレイでは、文字盤上の情報が装着者以外の人々に見える可能性があります。他人に見られたくない情報を隠す手段をユーザに確実に提供してください。[常時表示](/jp/design/human-interface-guidelines/always-on)のガイダンスを参照してください。

**データをアップデートするタイミングを注意深く検討する。** コンプリケーションのデータはタイムライン形式で提供し、各エントリーの値でデータをいつ文字盤に表示するかを指定します。データセットが異なれば、必要な時間の値も異なる可能性があります。例えば、会議アプリでは次の会議の情報を開始時刻の1時間前に表示するのが一般的でも、天気予報アプリでは気象の変化が予測された時点で予報を表示するのが普通です。タイムラインは1日あたりの上限回数までアップデートでき、システムにはアプリごとに定められた上限までタイムラインエントリーを保存します。そのため、データの利便性が高くなるタイミングを選ぶ必要があります。デベロッパ向けのガイダンスは、[ClockKitのコンプリケーションをWidgetKitに移行する方法](/documentation/WidgetKit/Converting-A-ClockKit-App#Configure-your-timeline-provider)を参照してください。

## [視覚的なデザイン](/jp/design/human-interface-guidelines/complications#Visual-design)

**表示するデータに合わせてリングまたはゲージスタイルを選ぶ。** 多くのファミリーはリングまたはゲージレイアウトに対応しているので、時間の経過に伴って変化していく数値を一貫した方法で表せます。以下に例を示します:

  * 閉じたスタイルは、全体に占める割合を表すのに便利です。これはバッテリー残量などが該当します。

  * 開いたスタイルは、最小値と最大値が不定の場合、つまり全体に占める割合を表していない場合に適しています。これはスピードメーターなどが該当します。

  * 開いたスタイルに類似したセグメントスタイルは、アプリで定義された範囲の値を表し、目まぐるしく変化する値にも対応できます。これはノイズを示すコンプリケーションなどが該当します。

**淡色モードでも画像が見た目よく表示されるようにする。** 淡色モードでは、コンプリケーションのテキスト、ゲージ、画像は単色で表現されます。フルカラー画像の場合は、その淡色バージョンが別途提供されない限り、彩度を落として表示されますデベロッパ向けのガイダンスは、[`WidgetRenderingMode`](/documentation/WidgetKit/WidgetRenderingMode)を参照してください。（レガシーテンプレートを使っている場合、淡色モードはグラフィックコンプリケーションにのみ適用されます）。淡色モードでコンプリケーションを効果的に機能させるには以下を参考にしてください:

  * 色が重要な情報を伝える唯一の方法にならないようにします。淡色モードでも非淡色モードでもユーザが同じ情報を取得できるようにしてください。

  * 必要に応じて、フルカラー画像の代替として淡色モードバージョンを提供します。フルカラー画像の彩度を落とすと見た目が悪くなる場合は、画像の別バージョンを淡色モード用に提供できます。

**フルカラーよりも淡色モードのコンプリケーションを好むユーザがいる可能性を認識する。** ユーザが淡色モードを選択すると彩度が自動的に低下し、コンプリケーションはグレイスケールに変換され、画像、ゲージ、およびテキストはユーザが選択した色に基づいた単色で表現されます。

**原則としてコンプリケーションコンテンツの線の幅は2ポイント以上にする。** これより細い線の場合、特に装着者が動いていると、一目では認識しにくくなる可能性があります。画像のサイズや複雑さに応じて、適切な線の太さを使ってください。

**対応している各コンプリケーション用に静的なプレースホルダ画像を提供する。** コンプリケーションデータとしてほかに表示するコンテンツがない場合は、プレースホルダ画像が使用されます。例えば、ユーザがアプリを初めてインストールしたときに、代わりに使用できるローカライズされたプレースホルダをアプリが生成できるかをシステムがチェックしている間、静的なプレースホルダを表示することができます。プレースホルダ画像は、ユーザがコンプリケーションを選択するカルーセルにも表示される場合があります。コンプリケーション画像のサイズはレイアウトごと（またはレガシーテンプレートごと）に異なるため、プレースホルダ画像のサイズが、対象のコンプリケーション用に提供する実際の画像のサイズと合わない可能性がある点に注意してください。デベロッパ向けのガイダンスは、[`placeholder(in:)`](/documentation/WidgetKit/TimelineProvider/placeholder\(in:\))を参照してください。

## [円形](/jp/design/human-interface-guidelines/complications#Circular)

円形レイアウトでは、インフォグラフおよびインフォグラフモジュラーの文字盤上の円形の領域にテキスト、ゲージ、フフルカラー画像を表示できます。円形ファミリーには、特大文字盤用の特大レイアウトも定義されています。

![赤い円の中に白い音符のアイコンがあります。現在の進捗状況を示すコンプリケーションで、円の外周の約90パーセントが鮮やかな赤で、残りの約10パーセントが暗い赤で表示されています。](https://docs-assets.developer.apple.com/published/5fe0f1a116f0b7d20b4b7b42ce7f5061/circular-closed-gauge-image%402x.png)閉じたゲージ画像

![緑の円の中に白いテキストで100と表示されています。現在の進捗状況を示すコンプリケーションで、円の外周が開始点から約5パーセントの位置まで重なっています。](https://docs-assets.developer.apple.com/published/ad2f10249867083a9859d8072ae7dd92/circular-closed-gauge-text%402x.png)閉じたゲージテキスト

![部分的な円周の内側に白いテキストで1.0と表示されています。円周は8時あたりの位置から始まり、4時あたりの位置で終わります。部分的な円周の色は、8時の開始点の緑から4時の終了点の紫まで徐々に変化しています。小さい緑の太陽のアイコンが6時の位置にあります。](https://docs-assets.developer.apple.com/published/a35c0dfe8b84d9856e957f1d9074ad54/circular-open-gauge-image%402x.png)開いたゲージ画像

![部分的な円周の内側に白いテキストで42と表示されています。円周は8時あたりの位置から始まり、4時あたりの位置で終わります。部分的な円周の色は、8時の開始点の青から4時の終了点の紫まで徐々に変化しています。6時の位置に緑の文字でAQIと表示されています。](https://docs-assets.developer.apple.com/published/da3ae62c880b2baa6ddc030116a8a7cc/circular-open-gauge-simple-text%402x.png)開いたゲージテキスト

![部分的な円周の内側に白いテキストで72と表示されています。円周は8時あたりの位置から始まり、4時あたりの位置で終わります。部分的な円周の色は、8時の開始点の緑から4時の終了点の黄色まで徐々に変化しています。2つの数値が6時の位置の左右にあります。左側に緑のテキストで55、右側にオレンジのテキストで76とあります。](https://docs-assets.developer.apple.com/published/55db7cc9a7377d63ab79b9a0e943e7ee/circular-open-gauge-range-text%402x.png)開いたゲージ範囲

![呼吸アプリアイコン。](https://docs-assets.developer.apple.com/published/803cb6b0e086101812af9549670d29a4/graphic-circular-image%402x.png)画像

![午後7時24分を示す時刻の上の日没を表すアイコンが円形領域の中央に配置されています。](https://docs-assets.developer.apple.com/published/ef675f451a5125fe56dc62a1d3b391d1/complication-graphic-circular-stack%402x.png)スタック画像

![2行のテキストが円形領域の中央に表示されています。上の行の白いテキストはAppleの銘柄コードAAPL、下の行は緑の数値で121.96となっています。](https://docs-assets.developer.apple.com/published/7f0cf0622839d5f9eabb5adc8aa063af/complication-graphic-circular-stack-text%402x.png)スタックテキスト

インフォグラフなどの文字盤でベゼルの丸みに沿ってテキストが並ぶデザインを使って、通常サイズの円形画像にテキストを付加することもできます。ベゼルの周囲ほぼ180度までであれば、テキスト切れなしで表示できます。

![円周の上3分の1に沿って白いテキストが表示されています。「午前8:00にヨガ、フロースタジオ」と表示されています。そのテキストの下の円形の領域に23日金曜日という日付があります。](https://docs-assets.developer.apple.com/published/3104b36c551c63e2ba02ee4494569470/bezel-circular-text%402x.png)閉じたゲージ画像

通常サイズの円形コンプリケーション画像をデザインする目安として、以下の値を使ってください。

画像| 40mm| 41mm| 44mm| 45mm/49mm  
---|---|---|---|---  
画像| 42x42 pt（84x84 px @2x）| 44.5x44.5 pt（89x89 px @2x）| 47x47 pt（94x94 px @2x）| 50x50 pt（100x100 px @2x）  
閉じたゲージ| 27x27 pt（54x54 px @2x）| 28.5x28.5 pt（57x57 px @2x）| 31x31 pt（62x62 px @2x）| 32x32 pt（64x64 px @2x）  
開いたゲージ| 11x11 pt（22x22 px @2x）| 11.5x11.5 pt（23x23 px @2x）| 12x12 pt（24x24 px @2x）| 13x13 pt（26x26 px @2x）  
スタック（テキスト以外）| 28x14 pt（56x28 px @2x）| 29.5x15 pt（59X30 px @2x）| 31x16 pt（62x32 px @2x）| 33.5x16.5 pt（67x33 px @2x）  
  
注意

画像にはシステムにより丸いマスクが適用されます。

通常サイズの円形コンプリケーションを実装しているSwiftUIビューでは、デフォルトでは以下のテキスト値が使用されます:

  * スタイル: ラウンド

  * 線の太さ: ミディアム

  * テキストサイズ: 12 pt（40mm）、12.5 pt（41mm）、13 pt（44mm）、14.5 pt（45mm/49mm）

連絡先の写真が表示される連絡先コンプリケーションなどで、特大文字盤に重要な情報を大きく表示できるデザインにしたい場合は、円形ファミリーレイアウトの特大バージョンを使用します。以下に示すレイアウトで、特大文字盤の大部分を占有する大きな円形の領域に、フルカラー画像、テキスト、ゲージを表示できます。一部のテキストフィールドはマルチカラーのテキストに対応します。

![赤い円の中に白い音符のアイコンがあります。現在の進捗状況を示すコンプリケーションで、円の外周の約66パーセントが鮮やかな赤で、残りの約34パーセントが暗い赤で表示されています。](https://docs-assets.developer.apple.com/published/7995bef71880b3feaf65229b13e056d0/complication-graphic-xl-circular-closed-gauge-image%402x.png)閉じたゲージ画像

![青い円の中に青いテキストで「85」という数字が1つ表示されています。現在の進捗状況を示すコンプリケーションで、円の外周の85パーセントが鮮やかな青で、残りの15パーセントが暗い青で表示されています。](https://docs-assets.developer.apple.com/published/1843423696d87ee883531f1249f8edb0/complication-graphic-xl-circular-closed-gauge-text%402x.png)閉じたゲージテキスト

![明るい青の部分的な円周の内側に明るい青のテキストで50、下の方に涙の形が表示されています。](https://docs-assets.developer.apple.com/published/d30dec30566ca11580b1875677ad2a50/complication-graphic-xl-circular-open-gauge-image%402x.png)開いたゲージ画像

![白い部分的な円周の内側に緑のテキストで29、下の方に緑のテキストでA、Q、Iと表示されています。](https://docs-assets.developer.apple.com/published/c67257046c83f99aaf792ee5962969d0/complication-graphic-xl-circular-open-gauge-simple-text%402x.png)開いたゲージテキスト

![部分的な円周の内側に白いテキストで56と表示されています。円周の色は8時の位置から4時の位置へ緑から赤に徐々に変わっています。部分的な円周の下の方で、2つの数値が横に並んでいます。左側に緑のテキストで52、右側に赤いテキストで89とあります。](https://docs-assets.developer.apple.com/published/0dd52bb02e302278972269c5cf478c2e/complication-graphic-xl-circular-open-gauge-range-text%402x.png)開いたゲージ範囲

![呼吸アプリアイコン。](https://docs-assets.developer.apple.com/published/a64c51056c2f87afc2f41bd274f57dc1/complication-graphic-xl-circular-image%402x.png)画像

![午後7時24分の上、円形領域の中央に日没の赤いアイコンが配置されています。](https://docs-assets.developer.apple.com/published/48362eaf1be0ea97de2cdc7744ff6dfd/complication-graphic-xl-circular-stack-image%402x.png)スタック画像

![2行のテキストが円形領域の中央に表示されています。上の行の白いテキストはAppleの銘柄コードAAPL、下の行は緑の数値で121.96となっています。](https://docs-assets.developer.apple.com/published/a35b148c62fc8a2ef8c13f6763dc4ddd/complication-graphic-xl-circular-stack-text%402x.png)スタックテキスト

特大の円形コンプリケーション画像を作成する目安として、以下の値を使ってください。

画像| 40mm| 41mm| 44mm| 45mm/49mm  
---|---|---|---|---  
画像| 120x120 pt（240x240 px @2x）| 127x127 pt（254x254 px @2x）| 132x132 pt（264x264 px @2x）| 143x143 pt（286x286 px @2x）  
開いたゲージ| 31x31 pt（62x62 px @2x）| 33x33 pt（66x66 px @2x）| 33x33 pt（66x66 px @2x）| 37x37 pt（74x74 px @2x）  
閉じたゲージ| 77x77 pt（154x154 px @2x）| 81.5x81.5 pt（163x163 px @2x）| 87x87 pt（174x174 px @2x）| 91.5x91.5 pt（183x183 px @2x）  
スタック| 80x40 pt（160x80 px @2x）| 85x42 pt（170x84 px @2x）| 87x44 pt（174x88 px @2x）| 95x48 pt（190x96 px @2x）  
  
注意

円形の開いたゲージおよび閉じたゲージの画像にはシステムにより丸いマスクが適用されます。

円形ファミリーのコンプリケーション用のコンテンツのないプレースホルダ画像を作成する目安として、以下の値を使ってください。

レイアウト| 38mm| 40mm/42mm| 41mm| 44mm| 45mm/49mm  
---|---|---|---|---|---  
円形| –| 42x42 pt（84x84 px @2x）| 44.5x44.5 pt（89x89 px @2x）| 47x47 pt（94x94 px @2x）| 50x50 pt（100x100 px @2x）  
ベゼル| –| 42x42 pt（84x84 px @2x）| 44.5x44.5 pt（89x89 px @2x）| 47x47 pt（94x94 px @2x）| 50x50 pt（100x100 px @2x）  
特大| –| 120x120 pt（240x240 px @2x）| 127x127 pt（254x254 px @2x）| 132x132 pt（264x264 px @2x）| 143x143 pt（286x286 px @2x）  
  
特大円形レイアウトを実装しているSwiftUIビューでは、以下のデフォルトのテキスト値が使用されます:

  * スタイル: ラウンド

  * 線の太さ: ミディアム

  * テキストサイズ: 34.5 pt（40mm）、36.5 pt（41mm）、36.5 pt（44mm）、41 pt（45mm/49mm）

## [コーナー](/jp/design/human-interface-guidelines/complications#Corner)

コーナーレイアウトでは、インフォグラフのような文字盤のコーナーにフルカラー画像、テキスト、ゲージを表示できます。一部のテンプレートはマルチカラーのテキストにも対応します。

![円形の領域内に黄色い太陽の一部が白い雲に隠れたアイコンがあります。](https://docs-assets.developer.apple.com/published/ab1d2d27241ee9c8c881935dfe3632dd/corner-circular-image%402x.png)円形画像

![14分59秒という値が単色で塗りつぶした曲線の横に表示されています。テキストと曲線は円周の右下4分の1に沿うような形状で配置されています。時間表示の下にはタイマーアプリアイコンがあります。](https://docs-assets.developer.apple.com/published/c8414636a2126011c53cd542330af39c/corner-gauge-image%402x.png)ゲージ画像

![気温（華氏）の値が緑で55、オレンジで76と表示され、その間にグラデーションで塗りつぶした曲線があります。曲線のグラデーションは値に合わせて緑からオレンジに変化します。テキストと曲線は円周の右上4分の1に沿うような形状で配置されています。華氏72度という値が気温の曲線の上に大きな白いテキストで表示されています。](https://docs-assets.developer.apple.com/published/57da1070e8a932159a67f930cd5efd03/corner-gauge-text%402x.png)ゲージテキスト

![2行のテキストが、円周の左上4分の1に沿うような形状で配置されています。上の行は、大きな白いテキストでCUPとなっています。下の行は、午前10時9分、+記号、0時間となっています。すべてオレンジのテキストです。](https://docs-assets.developer.apple.com/published/ec91687451acf3fd7f6bd3b04340dc30/corner-stack-text%402x.png)スタックテキスト

![オレンジのテキストで0時間0分0秒と表示されています。テキストは円周の左下4分の1に沿うような形状で配置されています。テキスト行の下にストップウォッチアプリアイコンがあります。](https://docs-assets.developer.apple.com/published/7e0e071264122740f727eb76c2ffefe3/corner-text-image%402x.png)テキスト画像

コーナーコンプリケーション画像をデザインする目安として、以下の値を使ってください。

画像| 40mm| 41mm| 44mm| 45mm/49mm  
---|---|---|---|---  
円形| 32x32 pt（64x64 px @2x）| 34x34 pt（68x68 px @2x）| 36x36 pt（72x72 px @2x）| 38x38 pt（76x76 px @2x）  
ゲージ| 20x20 pt（40x40 px @2x）| 21x21 pt（42x42 px @2x）| 22x22 pt（44x44 px @2x）| 24x24 pt（48x48 px @2x）  
テキスト| 20x20 pt（40x40 px @2x）| 21x21 pt（42x42 px @2x）| 22x22 pt（44x44 px @2x）| 24x24 pt（48x48 px @2x）  
  
注意

画像にはシステムにより丸いマスクが適用されます。

コーナーファミリーのコンプリケーション用のコンテンツのないプレースホルダ画像を作成する目安として、以下の値を使ってください。

38mm| 40mm/42mm| 41mm| 44mm| 45mm/49mm  
---|---|---|---|---  
–| 20x20 pt（40x40 px @2x）| 21x21 pt（42x42 px @2x）| 22x22 pt（44x44 px @2x）| 24x24 pt（48x48 px @2x）  
  
コーナーレイアウトを実装しているSwiftUIビューでは、以下のデフォルトのテキスト値が使用されます:

  * スタイル: ラウンド

  * 線の太さ: セミボールド

  * テキストサイズ: 10 pt（40mm）、10.5 pt（41mm）、11 pt（44mm）、12 pt（45mm/49mm）

## [インライン](/jp/design/human-interface-guidelines/complications#Inline)

インラインレイアウトには、実用的な小さいレイアウトと大きいレイアウトがあります。

実用的な小さいレイアウトを使えば、クロノグラフやシンプルなどの文字盤のコーナーにある長方形の領域を活用できます。コンテンツとして画像、インターフェイスアイコン、円グラフなどを配置できます。

![6時9分という時刻の上にLONという文字列が表示されています。](https://docs-assets.developer.apple.com/published/8570fb351b6cf5bdd6b14e2c234649c0/complication-utility-small-flat%402x.png)フラット

![2つの涙のアイコンが2つの部分的なリングの中央に配置されています。](https://docs-assets.developer.apple.com/published/b8f9c0fc6bbef48112d12622e7fe84b6/complication-utility-small-ring-image%402x.png)リングの画像

![2つの部分的なリングの中央に63という数字が表示されています。](https://docs-assets.developer.apple.com/published/9be2def9da342b62eaa23a94128f3c15/complication-utility-small-ring-text%402x.png)リングテキスト

![月の画像。](https://docs-assets.developer.apple.com/published/e7ce736c1f6f8a3b2621af2bb5e40193/complication-utility-small-square%402x.png)正方形

実用的な小さいレイアウトの画像をデザインする目安として、以下の値を使ってください。

コンテンツ| 38mm| 40mm/42mm| 41mm| 44mm| 45mm/49mm  
---|---|---|---|---|---  
フラット| 9-21x9 pt（18-42x18 px @2x）| 10-22x10 pt（20-44x20 px @2x）| 10.5-23.5x21 pt（21-47x21 px @2x）| N/A| 12-26x12 pt（24-52x24 px @2x）  
リング| 14x14 pt（28x28 px @2x）| 14x14 pt（28x28 px @2x）| 15x15 pt（30x30 px @2x）| 16x16 pt（32x32 px @2x）| 16.5x16.5 pt（33x33 px @2x）  
正方形| 20x20 pt（40x40 px @2x）| 22x22 pt（44x44 px @2x）| 23.5x23.5 pt（47x47 px @2x）| 25x25 pt（50x50 px @2x）| 26x26 pt（52x52 px @2x）  
  
実用的な大きいレイアウトは主にテキストベースですが、テキストの前にインターフェイスアイコンを表示することもできます。このレイアウトは、ユーティリティやモーションなどの文字盤の下部を広く使います。

![「午前11時 写真撮影会」というテキストが、大きいテキストサイズで1行に表示されています。](https://docs-assets.developer.apple.com/published/1fcf9505eaa3006b207d31f92d0680c3/complication-utility-large-flat%402x.png)フラット（大）

実用的な大きいレイアウトの画像をデザインする目安として、以下の値を使ってください。

コンテンツ| 38mm| 40mm/42mm| 41mm| 44mm| 45mm/49mm  
---|---|---|---|---|---  
フラット| 9-21x9 pt（18-42x18 px @2x）| 10-22x10 pt（20-44x20 px @2x）| 10.5-23.5x10.5 pt（21-47x21 px @2x）| N/A| 12-26x12 pt（24-52x24 px @2x）  
  
## [長方形](/jp/design/human-interface-guidelines/complications#Rectangular)

長方形レイアウトでは、大きい長方形の領域にフルカラー画像、テキスト、ゲージ、オプションのタイトルを表示できます。一部のテキストフィールドはマルチカラーのテキストに対応します。

大きい長方形の領域は、細かい情報を含むチャートやグラフ、図を表示できるので、時間の経過に伴って変化していく値やプロセスの詳細な情報を表示するのに適しています。例えば、心拍数コンプリケーションには過去24時間の心拍数のグラフが表示されます。このグラフでは、データを一目で把握できるように、コントラストの高い白と赤で主なコンテンツを表示し、コントラストの低いグレイでグラフの線とラベルを表示しています。

watchOS 10以降では、watchOSアプリの長方形レイアウトを作成した場合、それがスマートスタックに表示されることがあります。この表示を最適化するにはいくつかの方法があります:

  * 情報を伝えたり認知しやすくしたりするためのバックグラウンドカラーやバックグラウンドコンテンツを提供する

  * [インテント](https://developer.apple.com/documentation/appintents/app-intents)を使って関連性を指定し、最も妥当で便利なタイミングでスマートスタックにウィジェットが表示されるようにする

  * スマートスタックに最適化された、情報のカスタムレイアウトを作成する

デベロッパ向けのガイダンスは、[`WidgetFamily.accessoryRectangular`](/documentation/WidgetKit/WidgetFamily/accessoryRectangular)を参照してください。スマートスタックのウィジェットのデザインに関するその他のガイダンスは、[ウィジェット](/jp/design/human-interface-guidelines/widgets)を参照してください。

![左揃えの3行のテキスト。1行目は青いテキストでWater Reminders（水分摂取量）と表示されています。2行目は白いテキストで「32オンス摂取しました」と表示されています。3行目はグレイのテキストで「4日連続達成!」と表示されています。](https://docs-assets.developer.apple.com/published/769aff54f08a010dd1ec60efb7c64eed/rectangular-standard-body%402x.png)本文（標準）

![塗りつぶし部分で進捗状況を示すバーの上に2行のテキストが表示されています。1行目は青いテキストで、涙のアイコンの右にWater Reminder（水分摂取量）と表示されています。2行目は白いテキストで「32オンス摂取しました」と表示されています。バーは1行目のテキストと同じ青色で、左端から全体の約70パーセントの位置まで塗りつぶされています。](https://docs-assets.developer.apple.com/published/8db67e39c420e480f000ce7e80b49858/rectangular-text-gauge%402x.png)テキストゲージ

![グラフの上に1行のテキストが表示されています。テキストは白で68 BPM、それに続けて赤で2分前となっています。その下に、多数の心拍数データを時系列で示すグラフがあります。](https://docs-assets.developer.apple.com/published/3c4de88eb3b00995e9b491868641017d/rectangular-large-image%402x.png)大きい画像

長方形レイアウトの画像を作成する目安として、以下の値を使ってください。

コンテンツ| 40mm| 41mm| 44mm| 45mm/49mm  
---|---|---|---|---  
タイトル付きの大きい画像*| 150x47 pt（300x94 px @2x）| 159x50 pt（318x100 px @2x）| 171x54 pt（342x108 px @2x）| 178.5x56 pt（357x112 px @2x）  
タイトルなしの大きい画像*| 162x69 pt（324x138 px @2x）| 171.5x73 pt（343x146 px @2x）| 184x78 pt（368x156 px @2x）| 193x82 pt（386x164 px @2x）  
本文（標準）| 12x12 pt（24x24 px @2x）| 12.5x12.5 pt（25x25 px @2x）| 13.5x13.5 pt（27x27 px @2x）| 14.5x14.5 pt（29x29 px @2x）  
テキストゲージ| 12x12 pt（24x24 px @2x）| 12.5x12.5 pt（25x25 px @2x）| 13.5x13.5 pt（27x27 px @2x）| 14.5x14.5 pt（29x29 px @2x）  
  
注意

大きい画像のいずれのレイアウトにも、4ポイントのコーナー半径が自動的に適用されます。

長方形レイアウトを実装しているSwiftUIビューでは、以下のデフォルトのテキスト値が使用されます:

  * スタイル: ラウンド

  * 線の太さ: ミディアム

  * テキストサイズ: 16.5 pt（40mm）、17.5 pt（41mm）、18 pt（44mm）、19.5 pt（45mm/49mm）

## [レガシーテンプレート](/jp/design/human-interface-guidelines/complications#Legacy-templates)

### [円形小型](/jp/design/human-interface-guidelines/complications#Circular-small)

円形小型テンプレートで、小さい画像や短いテキストを文字盤のコーナーに表示できます（例えば、カラー文字盤）。

![涙のアイコンが部分的なリングの中央に配置されています。](https://docs-assets.developer.apple.com/published/33895eb916a9e7bdcbc520ad18647263/complication-circular-small-ring-image%402x.png)リングの画像

![63という数字が部分的なリングの中央に配置されています。](https://docs-assets.developer.apple.com/published/62d2947105b8940f5c24bfbcb4c5796c/complication-circular-small-ring-text%402x.png)リングテキスト

![ストップウォッチのアイコンが円形領域の中央に表示されています。](https://docs-assets.developer.apple.com/published/e6c9b241964b1ef816b4d9cd56736fe1/complication-circular-small-simple-image%402x.png)シンプルな画像

![68という数字と度数を示す記号が円形領域の中央に表示されています。](https://docs-assets.developer.apple.com/published/f4406a66c7eab467bcad8a26876f9831/complication-circular-small-simple-text%402x.png)シンプルなテキスト

![午後7時24分を示す時刻の上の日没を表すアイコンが円形領域の中央に配置されています。](https://docs-assets.developer.apple.com/published/b74c9bc11e182adc01d5ec7a1b0baee1/complication-circular-small-stack-image%402x.png)スタック画像

![6時9分という時刻の上にLONという文字列が表示されています。](https://docs-assets.developer.apple.com/published/202bdebe076aedf68603fbc4cbc6079a/complication-circular-small-stack-text%402x.png)スタックテキスト

円形小型コンプリケーションの画像をデザインする目安として、以下の値を使ってください。

画像| 38mm| 40mm/42mm| 41mm| 44mm| 45mm/49mm  
---|---|---|---|---|---  
リング| 20x20 pt（40x40 px @2x）| 22x22 pt（44x44 px @2x）| 23.5x23.5 pt（47x47 px @2x）| 24x24 pt（48x48 px @2x）| 26x26 pt（52x52 px @2x）  
シンプル| 16x16 pt（32x32 px @2x）| 18x18 pt（36x36 px @2x）| 19x19 pt（38x38 px @2x）| 20x20 pt（40x40 px @2x）| 21.5x21.5 pt（43x43 px @2x）  
スタック| 16x7 pt（32x14 px @2x）| 17x8 pt（34x16 px @2x）| 18x8.5 pt（36x17 px @2x）| 19x9 pt（38x18 px @2x）| 19x9.5 pt（38x19 px @2x）  
プレースホルダ| 16x16 pt（32x32 px @2x）| 18x18 pt（36x36 px @2x）| 19x19 pt（38x38 px @2x）| 20x20 pt（40x40 px @2x）| 21.5x21.5 pt（43x43 px @2x）  
  
注意

スタックの各測定値の幅の値は最大値を表しています。

### [モジュラー小型](/jp/design/human-interface-guidelines/complications#Modular-small)

モジュラー小型テンプレートでは、アイコンとコンテンツで構成される2行のスタック、円グラフ、または単一の大きな項目を表示できます（例えば、モジュラー文字盤の下段のコンプリケーション）。

![2行のカラムにテキストと数字が配置されています。上の行は、CPという文字と14という数字です。下の行は、MHという文字と28という数字です。](https://docs-assets.developer.apple.com/published/539d608a87f5ce484e384e16f8820291/complication-modular-small-columns-text%402x.png)カラムテキスト

![涙のアイコンが部分的なリングの中央に配置されています。](https://docs-assets.developer.apple.com/published/4fc4ed5dc5ad3eca0b241da5ee4f7ade/complication-modular-small-ring-image%402x.png)リングの画像

![63という数字が部分的なリングの中央に配置されています。](https://docs-assets.developer.apple.com/published/e8d2d26f2a4a8487a93828446f2d15ac/complication-modular-small-ring-text%402x.png)リングテキスト

![月の画像。](https://docs-assets.developer.apple.com/published/8b985e64563432cdb87a8b37cea075e6/complication-modular-small-simple-image%402x.png)シンプルな画像

![68という数字と度数を示す記号。](https://docs-assets.developer.apple.com/published/4e39f1ca1f72f72dd598c0cca5426790/complication-modular-small-simple-text%402x.png)シンプルなテキスト

![午後7:24の上に表示された日没のアイコン。](https://docs-assets.developer.apple.com/published/d4ad86d72677b5a09199075a6712ef16/complication-modular-small-stack-image%402x.png)スタック画像

![6時9分という時刻の上にLONという文字列が表示されています。](https://docs-assets.developer.apple.com/published/792f254ca434b41d1277607776dba77f/complication-modular-small-stack-text%402x.png)スタックテキスト

モジュラー小型コンプリケーションのアイコンと画像をデザインする目安として、以下の値を使ってください。

画像| 38mm| 40mm/42mm| 41mm| 44mm| 45mm/49mm  
---|---|---|---|---|---  
リング| 18x18 pt（36x36 px @2x）| 19x19 pt（38x38 px @2x）| 20x20 pt（40x40 px @2x）| 21x21 pt（42x42 px @2x）| 22.5x22.5 pt（45x45 px @2x）  
シンプル| 26x26 pt（52x52 px @2x）| 29x29 pt（58x58 px @2x）| 30.5x30.5 pt（61x61 px @2x）| 32x32 pt（64x64 px @2x）| 34.5x34.5 pt（69x69 px @2x）  
スタック| 26x14 pt（52x28 px @2x）| 29x15 pt（58x30 px @2x）| 30.5x16 pt（61x32 px @2x）| 32x17 pt（64x34 px @2x）| 34.5x18 pt（69x36 px @2x）  
プレースホルダ| 26x26 pt（52x52 px @2x）| 29x29 pt（58x58 px @2x）| 30.5x30.5 pt（61x61 px @2x）| 32x32 pt（64x64 px @2x）| 34.5x34.5 pt（69x69 px @2x）  
  
注意

スタックの各測定値の幅の値は最大値を表しています。

### [モジュラー大型](/jp/design/human-interface-guidelines/complications#Modular-large)

モジュラー大型テンプレートの広いキャンバスに最大3行のコンテンツを表示できます（例えば、モジュラー文字盤の中段）。

![3行のカラムにアクティビティ関連の情報が表示されています。上の行は、660分の396というカロリー測定値です。中間の行は、30分の13という分の測定値です。下の行は、12分の3という時間の測定値です。](https://docs-assets.developer.apple.com/published/4e4702d1120b90845deca35c8434e9e9/complication-modular-large-columns%402x.png)カラム

![左揃えの3行のテキストに天気関連の情報が表示されています。上の行は、カリフォルニア州クパチーノという場所です。中間の行は、華氏68度で曇りという情報です。下の行は、最高華氏72度、最低華氏62度という予報値です。](https://docs-assets.developer.apple.com/published/b8412904cc9bad82feac3a27985d0bf8/complication-modular-large-standard-body%402x.png)本文（標準）

![タイトルの付いた2列x2行の表にスポーツ関連の情報が表示されています。表のタイトルは「最終スコア」です。1行目は、14という数字とCentral Prepというテキストです。2行目は、28という数字とMission Highというテキストです。](https://docs-assets.developer.apple.com/published/e55417646b6cc4c99ec07be075cd07e6/complication-modular-large-table%402x.png)表

![両端揃えの2行のテキストにカレンダー関連の情報が表示されています。1行目は水曜日と表示されています。2行目には、3月の短縮形であるMarと数字の9が表示され、1行目の約2倍の高さのテキストになっています。](https://docs-assets.developer.apple.com/published/ecdadad624fd7f5c79cd071719b5a137/complication-modular-large-tall-body%402x.png)本文（高）

モジュラー大型コンプリケーションのアイコンと画像をデザインする目安として、以下の値を使ってください。

コンテンツ| 38mm| 40mm/42mm| 41mm| 44mm| 45mm/49mm  
---|---|---|---|---|---  
カラム| 11-32x11 pt（22-64x22 px @2x）| 12-37x12 pt（24-74x24 px @2x）| 12.5-39x12.5 pt（25-78x25 px @2x）| 14-42x14 pt（28-84x28 px @2x）| 14.5-44x14.5 pt（29-88x29 px @2x）  
本文（標準）| 11-32x11 pt（22-64x22 px @2x）| 12-37x12 pt（24-74x24 px @2x）| 12.5-39x12.5 pt（25-78x25 px @2x）| 14-42x14 pt（28-84x28 px @2x）| 14.5-44x14.5 pt（29-88x29 px @2x）  
表| 11-32x11 pt（22-64x22 px @2x）| 12-37x12 pt（24-74x24 px @2x）| 12.5-39x12.5 pt（25-78x25 px @2x）| 14-42x14 pt（28-84x28 px @2x）| 14.5-44x14.5 pt（29-88x29 px @2x）  
  
### [特大](/jp/design/human-interface-guidelines/complications#Extra-large)

特大テンプレートで、より大きいテキストと画像を（例えば、特大文字盤に）表示できます。

![涙のアイコンが部分的なリングの中央に配置されています。](https://docs-assets.developer.apple.com/published/586c9324ec9f5877de7b76d22d74829c/complication-extralarge-ring-image%402x.png)リングの画像

![63という数字が部分的なリングの中央に配置されています。](https://docs-assets.developer.apple.com/published/b89b3b2763975eb4006f7bf7ec12fa24/complication-extralarge-ring-text%402x.png)リングテキスト

![月の画像。](https://docs-assets.developer.apple.com/published/ecc4e04193af3c88d00b7b41919b5ab1/complication-extralarge-simple-image%402x.png)シンプルな画像

![68という数字と度数を示す記号。](https://docs-assets.developer.apple.com/published/5a80ff98da9d901f28a85623be27c973/complication-extralarge-simple-text%402x.png)シンプルなテキスト

![午後7:24の上に表示された日没のアイコン。](https://docs-assets.developer.apple.com/published/ff21f994ff7434bcba8d3f6aeaae3c19/complication-extralarge-stack-image%402x.png)スタック画像

![6時9分という時刻の上にLONという文字列が表示されています。](https://docs-assets.developer.apple.com/published/505f8b28aa870ebaf42ce750af9f0065/complication-extralarge-stack-text%402x.png)スタックテキスト

特大コンプリケーションのアイコンと画像をデザインする目安として、以下の値を使ってください。

画像| 38mm| 40mm/42mm| 41mm| 44mm| 45mm/49mm  
---|---|---|---|---|---  
リング| 63x63 pt（126x126 px @2x）| 66.5x66.5 pt（133x133 px @2x）| 70.5x70.5 pt（141x141 px @2x）| 73x73 pt（146x146 px @2x）| 79x79 pt（158x158 px @2x）  
シンプル| 91x91 pt（182x182 px @2x）| 101.5x101.5 pt（203x203 px @2x）| 107.5x107.5 pt（215x215 px @2x）| 112x112 pt（224x224 px @2x）| 121x121 pt（242x242 px @2x）  
スタック| 78x42 pt（156x84 px @2x）| 87x45 pt（174x90 px @2x）| 92x47.5 pt（184x95 px @2x）| 96x51 pt（192x102 px @2x）| 103.5x53.5 pt（207x107 px @2x）  
プレースホルダ| 91x91 pt（182x182 px @2x）| 101.5x101.5 pt（203x203 px @2x）| 107.5x107.5 pt（215x215 px @2x）| 112x112 pt（224x224 px @2x）| 121x121 pt（242x242 px @2x）  
  
注意

スタックの各測定値の幅の値は最大値を表しています。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/complications#Platform-considerations)

 _iOS、iPadOS、macOS、tvOS、visionOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/complications#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/complications#Related)

[文字盤](/jp/design/human-interface-guidelines/watch-faces)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/complications#Developer-documentation)

[WidgetKit](/documentation/WidgetKit)

#### [ビデオ](/jp/design/human-interface-guidelines/complications#Videos)

[](https://developer.apple.com/videos/play/wwdc2023/10309)

[](https://developer.apple.com/videos/play/wwdc2022/10051)

[](https://developer.apple.com/videos/play/wwdc2022/10050)

## [変更履歴](/jp/design/human-interface-guidelines/complications#Change-log)

日付| 変更内容  
---|---  
2023年10月24日| 非推奨になったClockKitドキュメントへのリンクをWidgetKitドキュメントへのリンクに置換。  
2023年6月05日| スマートスタックにウィジェットとして表示されるようにするための長方形コンプリケーションのガイダンスを更新。  
2022年9月14日| Apple Watch Ultraの仕様を追加。
