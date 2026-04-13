# visionOS向けのデザイン

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/designing-for-visionos

# visionOS向けのデザイン

Apple Vision Proを装着すると、周囲の環境とのつながりを保ったまま、無限の3D空間の中でアプリやゲームを使うことができます。

![図案化されたApple Vision Proがグリッド上に表示されています。画像の上に長方形と円形のグリッド線が重ねられており、画像全体が6色の初代Appleロゴの緑を連想させる緑色を帯びています。](https://docs-assets.developer.apple.com/published/9d51f701c7321cced431aac9d5212b9e/platforms-visionOS-intro%402x.png)

visionOS向けのアプリやゲームをデザインするときは、まず、このプラットフォームを特徴付ける基本的なデバイスの性質とパターンを理解することから始めましょう。この性質とパターンを活かしてデザインを決定していくことで、引き込まれるようなイマーシブ体験を作ることができます。

**空間。** Apple Vision Proでは、無限大のキャンバスを使って、[ウインドウ](/jp/design/human-interface-guidelines/windows)、[ボリューム](/jp/design/human-interface-guidelines/windows#visionOS-volumes)、3Dオブジェクトなどの仮想コンテンツを見たり、体験のイマーシブ感を高めて別の場所に移動したような感覚を味わったりできます。

**イマーシブ感。** visionOSアプリでは、[イマーシブ感](/jp/design/human-interface-guidelines/immersive-experiences)の度合いを滑らかに切り替えることができます。アプリは、デフォルトでは _共有スペース_ で起動します。ここでは、複数のアプリを並べて開くことができるほか、ウインドウを開く、閉じる、移動するといった操作ができます。また、ユーザが選択すれば、1つのアプリだけが実行される _フルスペース_ にアプリを移行させることも可能です。 フルスペースに移行したアプリでは、3Dコンテンツを周囲の環境に溶け込ませて表示したり、別の場所を見ることができるポータルを開いたり、別の世界に入ったりすることができます。

**パススルー。**[パススルー](/jp/design/human-interface-guidelines/immersive-experiences#Immersion-and-passthrough)は、デバイスの外部カメラからのライブビデオを表示します。これにより、現実世界の周囲の環境を見ながら仮想コンテンツを操作することが可能になります。周囲の環境の表示量を増減するには、[Digital Crown](/jp/design/human-interface-guidelines/digital-crown)を使ってパススルーの量を調整します。

**空間オーディオ。** Apple Vision Proは、音響センシングとビジュアルセンシングの技術を組み合わせてユーザの周囲の音特性をモデル化することで、空間内でのオーディオの聞こえ方が自然なものになるように自動的に処理します。周囲の環境に関する情報へのアクセスをユーザがアプリに許可した場合は、アプリ側で[空間オーディオ](/jp/design/human-interface-guidelines/playing-audio#visionOS)を細かく調整してカスタム体験にリアリティを出すことができます。

**視線と手。** 通常、ほとんどのアクションは、[視線](/jp/design/human-interface-guidelines/eyes)で仮想オブジェクトを注視してから、タップなどの _間接的_ な[ジェスチャ](/jp/design/human-interface-guidelines/gestures#visionOS)を使ってアクティベートすることで実行します。そのほか、指でタッチするなどの _ダイレクト_ ジェスチャを使って仮想オブジェクトを操作することもできます。

**人間工学。** Apple Vision Proの装着中は、現実のものも仮想オブジェクトもすべてデバイスのカメラを通して見ることになるので、視覚的に快適に使えるようにすることが最も重要です。快適さを保つため、システムは、ユーザの身長や体勢（座っているか、立っているか、横になっているか）にかかわらず、自動的に装着者の頭を基準にしてコンテンツを配置します。ユーザがコンテンツに近づくのではなく、visionOSがコンテンツをユーザのところまで持ってきてくれるため、アプリもゲームもリラックスした姿勢で操作することができます。

**アクセシビリティ。** Apple Vision Proは、VoiceOver、スイッチコントロール、滞留コントロール、アクセスガイド、ヘッドポインタなどさまざまな[アクセシビリティ](/jp/design/human-interface-guidelines/accessibility)に対応しているため、ユーザは自分に都合のよい操作方法を選ぶことができます。ほかのすべてのプラットフォームと同様に、visionOSにも、デフォルトでアクセシビリティに対応しているシステム定義のUIコンポーネントのほか、アプリやゲームのアクセシビリティを強化するためのシステムフレームワークが用意されています。

重要

Apple Vision Proのアプリを開発する際は、このデバイスや空間コンピューティング環境の特徴や特性を必ず考慮し、ユーザの安全性に特に注意してください。詳しくは、[Apple Vision Proユーザガイド](https://support.apple.com/guide/apple-vision-pro)を参照してください。例えば、自動車の運転中や重機の操作中にApple Vision Proを使用するべきではありません。また、ベランダ、道路、階段の付近など、身の危険が潜む可能性があり、安全を確保できない場所での移動中に使用することも想定していません。13歳未満のユーザがApple Vision Proを装着して使用することは想定していません。

## [ベストプラクティス](/jp/design/human-interface-guidelines/designing-for-visionos#Best-practices)

visionOSのアプリやゲームを優れたものにするには、美しいコンテンツや、今までにない機能、夢中になれる冒険などのイマーシブな空間に入ることができる驚きの体験を実現しつつ、分かりやすく馴染みのある体験を作りましょう。

**Apple  Vision Proの独自機能を活かす。**空間、空間オーディオ、イマーシブ感を活かして体験に命を吹き込むと共に、パススルーや視線と手による空間入力を取り入れてリラックスした状態でデバイスを使えるようにしましょう。

**アプリの最も特徴的な機能の提示方法をデザインするときはさまざまなタイプのイマーシブ度を検討する。** アプリの体験は、UIを中心としたウインドウ形式で提示することも、完全なイマーシブ体験として提示することも、その中間の形で提示することもできます。アプリの重要な機能のそれぞれについて、最低限これだけのイマーシブ度があれば最適に使えるというところを見つけてください。あらゆる側面を完全イマーシブ型にしなければならないと考える必要はありません。

**限られた領域で完結するUI中心の体験にはウインドウを使う。** 標準的なタスクを実行しやすくするには、空間内に平面として表示され、馴染みのあるコントロールを含めることができる[ウインドウ](/jp/design/human-interface-guidelines/windows#visionOS)を使いましょう。visionOSでは、ユーザがウインドウをどこにでも移動することができ、どの距離にあるウインドウのコンテンツも[ダイナミックスケーリング](/jp/design/human-interface-guidelines/spatial-layout#Scale)によって読みやすさが保たれます。

**快適性を優先する。** 身体に負担をかけずにリラックスした姿勢でアプリやゲームを操作できるようにするには、以下の基本を念頭に置きましょう。

  * ユーザの頭を基準にして、ユーザの[視野](/jp/design/human-interface-guidelines/spatial-layout#Field-of-view)の中にコンテンツを表示する。頭の向きを変えたり移動したりしないと操作できないような場所にコンテンツを配置するのは避けてください。

  * 過度な[モーション](/jp/design/human-interface-guidelines/motion#visionOS)、不快なモーション、速すぎるモーション、座標系が静止していないモーションを表示することは避ける。

  * 手を膝の上や身体の横に置いたままアプリを操作することができる[間接的ジェスチャ](/jp/design/human-interface-guidelines/gestures#visionOS)に対応する。

  * 直接的ジェスチャに対応する場合は、インタラクティブなコンテンツを遠すぎる場所に配置したり、ユーザに長時間操作させたりしないようにする。

  * ユーザが完全な[イマーシブ体験](/jp/design/human-interface-guidelines/immersive-experiences)にいるときにはあまり移動を促さない。

**アクティビティをほかのユーザと共有できるようにする。**[SharePlay](/jp/design/human-interface-guidelines/shareplay#visionOS)を使ってアクティビティの共有を可能にした場合は、ほかの参加者の _空間Persona_ を見ることができるので、ユーザは全員で同じ空間にいる感覚を味わうことができます。

## [リソース](/jp/design/human-interface-guidelines/designing-for-visionos#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/designing-for-visionos#Related)

[Appleデザインリソース](https://developer.apple.com/design/resources/#visionos-apps)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/designing-for-visionos#Developer-documentation)

[visionOS Pathway](https://developer.apple.com/visionos/get-started/)

[初めてのvisionOSアプリの作成](/documentation/visionOS/creating-your-first-visionos-app)

#### [ビデオ](/jp/design/human-interface-guidelines/designing-for-visionos#Videos)

[](https://developer.apple.com/videos/play/wwdc2024/10096)

[](https://developer.apple.com/videos/play/wwdc2024/10086)

[](https://developer.apple.com/videos/play/wwdc2023/10072)

## [変更履歴](/jp/design/human-interface-guidelines/designing-for-visionos#Change-log)

日付| 変更内容  
---|---  
2024年2月02日| Apple Vision Proユーザガイドのリンクを追加。  
2023年9月12日| イントロアートワークをアップデート。  
2023年6月21日| 新規ページ。
