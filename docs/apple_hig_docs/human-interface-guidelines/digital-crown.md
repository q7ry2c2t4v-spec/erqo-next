# Digital Crown

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/digital-crown

# Digital Crown

Digital Crownは、Apple Vision ProとApple Watchの重要なハードウェア入力装置です。

![Digital Crownの横にあるカーブした矢印のスケッチ。Digital Crownの回転を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる紫色になっています](https://docs-assets.developer.apple.com/published/5f735191138feccc22bb03cf971be9e4/inputs-digital-crown-intro%402x.png)

Apple Vision ProとApple Watchでは、Digital Crownを使ってシステムを操作することができます。Apple Watchの場合は、Digital Crownでアプリを操作することも可能です。

![Apple Vision Proを装着している人の頭部のクローズアップ写真。人差し指でDigital Crownを指しています。](https://docs-assets.developer.apple.com/published/b421afd55a6401eeacedaa088b02d909/digital-crown-apple-vision-pro%402x.png)Apple Vision ProのDigital Crown

![Apple Watchを斜めから見たクローズアップ写真。Digital Crownが画像の中央で強調されています。](https://docs-assets.developer.apple.com/published/8a6cff758555d19f9aa789f623693495/digital-crown-apple-watch%402x.png)Apple WatchのDigital Crown

## [Apple Vision Pro](/jp/design/human-interface-guidelines/digital-crown#Apple-Vision-Pro)

Apple Vision Proでは、Digital Crownを使って以下のことができます。

  * 音量を調整する

  * ポータルや環境、またはフルスペースで実行中のアプリやゲームでイマーシブ度を調整する（ガイダンスは[イマーシブ体験](/jp/design/human-interface-guidelines/immersive-experiences)を参照してください）

  * コンテンツの中心を設定し直して自分の正面に来るようにする

  * 「アクセシビリティ」設定を開く

  * アプリを閉じてホーム表示に戻る

## [Apple Watch](/jp/design/human-interface-guidelines/digital-crown#Apple-Watch)

ユーザがDigital Crownを回したときに生成される情報（標準コントロールやカスタムコントロールのスクロールや操作など）は、アプリの操作を強化したり円滑にしたりするために使用できます。

watchOS 10以降ではDigital Crownの役割が強化され、ナビゲーションの主な入力手段になりました。ユーザがDigital Crownを回すと、文字盤ではスマートスタックにウィジェットが表示され、ホーム画面ではアプリのコレクションを縦方向に閲覧できます。アプリ内では、Digital Crownを回して、縦方向にページ化されたタブを切り替えたり、リスト表示や高さが可変のページをスクロールしたりできます。

このようなナビゲーション機能のほかに、Digital Crownを回して、アプリの操作性の強化やシンプル化に利用できる情報を生成することも可能です。Digital Crownを回して、データを調べたり、標準コントロールやカスタムコントロールを操作したりできるのです。

注意

ユーザがDigital Crownを押してもアプリでは応答できません。この操作は、ホーム画面の表示のようなシステムが提供する機能用という形でwatchOS内で指定されています。

Apple WatchのほとんどのモデルではDigital Crownが触覚フィードバックを返すので、ユーザはコンテンツのスクロールをより触覚的に感じることができます。デフォルトでは、ユーザがDigital Crownを回すと、カチッカチッという連続的な触覚 _フィードバック_ （タップ）が返ってきます。テーブルビューなど、システムのコントロールによっては、スクロールによって新しい項目が画面に入ってくるときに同じフィードバックが提供されます。

**アプリのナビゲーション操作をDigital Crownに集約して固定する。** watchOS 10以降では、Digital Crownを回す操作が、アプリ内およびアプリ間の主要なナビゲーション手段になります。リスト表示、タブ表示、スクロール表示は縦方向で、ユーザはDigital Crownを使って、アプリのインターフェイスの主要な要素間を簡単に移動できます。これらの操作をDigital Crownで可能にする場合は、対応するタッチ画面操作でも必ず提供してください。

**ナビゲーションが不要なコンテキストで、Digital Crownを使用してデータを調べられるようにする。** Digital Crownを使ってリスト内やページ間を移動する必要がないコンテキストでは、Digital Crownをアプリ内のデータを調べるための便利なツールとして利用できます。例えば「世界時計」の場合、Digital Crownを回すと選択中の場所の時刻が進み、さまざまな時刻と現在時刻を比較することができます。

**Digital Crownの操作時に視覚的なフィードバックを返す。** 例えば、ユーザによるDigital Crownの操作に合わせて、ピッカーに現在表示されている値を変化させます。Digital Crownの回転を直接トラッキングすることで、そのデータを使ってプログラム側でインターフェイスをアップデートすることができます。視覚的なフィードバックを返さないと、このアプリはDigital Crownを回しても反応しないとユーザに思われる可能性があります。

**ユーザがDigital Crownを回すスピードに合わせてインターフェイスをアップデートする。** ユーザは、Digital Crownの回転がインターフェイスの制御に正確に反映されることを期待します。この回転スピードに基づいて、インターフェイスを変化させるスピードを決定すると効果的です。ただし、値の選択が困難になるような速度でコンテンツの表示をアップデートすることは避けてください。

**デフォルトの触覚フィードバックは、アプリに適している場合に使用する。** 触覚フィードバックがアプリの使用状況に合うとは思えない場合、例えば、デフォルトの機械的なフィードバックがアプリのアニメーションと合わない場合は、そのフィードバックをオフにしてください。また、テーブルのスクロールで使う触覚フィードバックの動作を調整し、行単位ではなく連続的なフィードバックを返すようにすることもできます。例えば、表を構成する各行の高さに大幅な違いがある場合は、連続的なフィードバックの方が一貫した操作感が得られると考えられます。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/digital-crown#Platform-considerations)

 _iOS、iPadOS、macOS、tvOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/digital-crown#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/digital-crown#Related)

[フィードバック](/jp/design/human-interface-guidelines/feedback)

[アクションボタン](/jp/design/human-interface-guidelines/action-button)

[イマーシブ体験](/jp/design/human-interface-guidelines/immersive-experiences)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/digital-crown#Developer-documentation)

[`WKCrownDelegate`](/documentation/WatchKit/WKCrownDelegate) — WatchKit

## [変更履歴](/jp/design/human-interface-guidelines/digital-crown#Change-log)

日付| 変更内容  
---|---  
2023年12月05日| Apple Vision ProとApple Watchのアートワークを追加し、Digital Crownからの情報をvisionOSアプリで直接受け取らないことを明確化。  
2023年6月21日| visionOSのガイダンスを追加するために更新。  
2023年6月05日| ナビゲーションにおけるDigital Crownの中心的な役割を強調するガイドラインを追加。
