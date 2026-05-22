# Flexible Isosurface Extraction for Gradient-Based Mesh Optimization

## 메타데이터

- PDF 파일: `Flexible Isosurface Extraction for Gradient-Based Mesh Optimization.pdf`
- 논문 제목: Flexible Isosurface Extraction for Gradient-Based Mesh Optimization
- 저자: Tianchang Shen, Jacob Munkberg, Jon Hasselgren, Kangxue Yin, Zian Wang, Wenzheng Chen, Zan Gojcic, Sanja Fidler, Nicholas Sharp, Jun Gao
- venue/arXiv: arXiv:2308.05371v1 [cs.GR]
- 연도: 2023
- DOI/URL: https://arxiv.org/abs/2308.05371
- 작업 일시: 2026-05-22 14:30

## Abstract

This work considers gradient-based mesh optimization, where we iteratively optimize for a 3D surface mesh by representing it as the isosurface of a scalar field, an increasingly common paradigm in applications including photogrammetry, generative modeling, and inverse physics.

**이 논문은 scalar field의 isosurface로 3D surface mesh를 표현하고 이를 반복적으로 최적화하는 gradient-based mesh optimization을 다루며, 이는 photogrammetry, generative modeling, inverse physics 같은 응용에서 점점 흔해지는 패러다임이다.**

Existing implementations adapt classic isosurface extraction algorithms like Marching Cubes or Dual Contouring; these techniques were designed to extract meshes from fixed, known fields, and in the optimization setting they lack the degrees of freedom to represent high-quality feature-preserving meshes, or suffer from numerical instabilities.

**기존 구현은 Marching Cubes나 Dual Contouring 같은 고전적 isosurface extraction 알고리즘을 변형해 쓰지만, 이 기법들은 고정되고 알려진 field에서 mesh를 추출하도록 설계되었기 때문에, optimization setting에서는 high-quality feature-preserving mesh를 표현할 자유도가 부족하거나 수치적 불안정성을 겪는다.**

We introduce FlexiCubes, an isosurface representation specifically designed for optimizing an unknown mesh with respect to geometric, visual, or even physical objectives.

**저자들은 geometric, visual, 나아가 physical objective에 대해 unknown mesh를 최적화하도록 특별히 설계된 isosurface representation인 FlexiCubes를 제안한다.**

Our main insight is to introduce additional carefully-chosen parameters into the representation, which allow local flexible adjustments to the extracted mesh geometry and connectivity.

**핵심 통찰은 representation에 신중히 선택한 추가 parameter들을 넣어, 추출된 mesh geometry와 connectivity를 local하게 유연하게 조정할 수 있게 하는 것이다.**

These parameters are updated along with the underlying scalar field via automatic differentiation when optimizing for a downstream task.

**이 parameter들은 downstream task를 최적화할 때 automatic differentiation을 통해 underlying scalar field와 함께 업데이트된다.**

We base our extraction scheme on Dual Marching Cubes for improved topological properties, and present extensions to optionally generate tetrahedral and hierarchically-adaptive meshes.

**저자들은 더 나은 topological property를 위해 extraction scheme을 Dual Marching Cubes에 기반시키고, 선택적으로 tetrahedral mesh와 hierarchically-adaptive mesh를 생성하는 확장도 제시한다.**

Extensive experiments validate FlexiCubes on both synthetic benchmarks and real-world applications, showing that it offers significant improvements in mesh quality and geometric fidelity.

**광범위한 실험은 synthetic benchmark와 real-world application 모두에서 FlexiCubes를 검증하며, mesh quality와 geometric fidelity가 크게 개선됨을 보인다.**

## 목차

> 본문 heading 기반으로 재구성했으며, section/subsection 누락 여부를 다시 확인했다.

1. Introduction
2. Related Work
   1. Isosurface Extraction
   2. Gradient-Based Mesh Optimization in ML
3. Background and Motivation
   1. Marching Cubes & Tetrahedra
   2. Dual Contouring
   3. Dual Marching Cubes
4. Method
   1. Dual Marching Cubes Mesh Extraction
   2. Flexible Dual Vertex Positioning
   3. Flexible Quad Splitting
   4. Flexible Grid Deformation
   5. Tetrahedral Mesh Extraction
   6. Adaptive Mesh Resolution
   7. Regularizers
5. Experiments
   1. Mesh Reconstruction
   2. Mesh Optimization with Regularizations
6. Applications
   1. Photogrammetry Through Differentiable Rendering
   2. Mesh Simplification of Animated Objects
   3. 3D Mesh Generation
   4. Differentiable Physics Simulation
7. Discussion
   1. Performance
   2. Limitations
   3. Future Work
8. Supplement
   1. Details on FlexiCubes
   2. Analysis
   3. Experimental Details
   4. Applications

## 요약

### 1. 전체 구조

이 논문은 differentiable mesh generation에서 **isosurface extraction layer 자체가 optimization landscape와 mesh quality를 결정한다**는 문제의식에서 출발한다. 일반적인 pipeline은 scalar function 또는 SDF를 grid 위에 두고, 그 $0$-level set을 triangle mesh로 추출한 뒤, rendering, geometry, physics loss를 mesh에 걸고 scalar field로 gradient를 되돌리는 구조다.

기존 Marching Cubes 계열은 gradient flow는 비교적 다루기 쉽지만 vertex가 grid edge zero-crossing에 묶여 sharp feature와 non-axis-aligned geometry를 잘 맞추기 어렵다. Dual Contouring은 cell 내부 vertex 배치로 sharp feature에는 강하지만 QEF 기반 vertex positioning이 optimization 중 불안정하거나 cell 밖으로 나갈 수 있다. DMTet은 differentiable extraction으로 널리 쓰이지만 sliver triangle과 feature alignment 문제가 남는다.

FlexiCubes는 Dual Marching Cubes의 topology를 기반으로 하면서, optimization 가능한 local degrees of freedom을 추가한다. 목표는 다음 두 속성을 동시에 만족하는 것이다.

- **Grad.** mesh에 대한 differentiation이 실용적으로 잘 작동하고 gradient-based optimization이 수렴한다.
- **Flexible.** vertex를 local하게 조정해 sharp feature와 고품질 tessellation을 적은 element 수로 표현한다.

### 2. Section 간 연결

Introduction은 high-quality mesh generation이 inverse rendering, generative modeling, physics simulation에서 중요하지만 기존 extraction method가 optimization용으로 설계되지 않았음을 제기한다. Related Work와 Background는 MC, DC, DMC, DMTet의 장단점을 분리해 설명하고, 특히 “fixed known field에서 extraction”과 “unknown field를 최적화하면서 반복 extraction”이 다른 문제임을 강조한다.

Method는 FlexiCubes의 세 가지 trainable parameter group을 제시한다. Experiments는 synthetic reconstruction에서 이 parameter들이 실제로 geometry accuracy와 triangle quality를 개선하는지 검증하고, Applications는 nvdiffrec, animated mesh simplification, GET3D, differentiable physics simulation에 plug-in 형태로 넣었을 때 downstream benefit이 있는지 확인한다. Discussion은 비용 증가, self-intersection, global continuity 한계를 정리한다.

### 3. 핵심 주장과 근거

논문의 핵심 주장은 **isosurface extractor에 제한된 추가 자유도를 넣으면 topology robustness를 크게 잃지 않으면서 differentiable mesh optimization의 표현력과 mesh quality를 동시에 개선할 수 있다**는 것이다.

근거는 네 층위로 제시된다.

1. DMC 기반 connectivity는 MC보다 dual vertex 배치가 유연하고, DC보다 manifoldness를 관리하기 쉽다.
2. Flexible vertex positioning, grid deformation, quad splitting을 ablation하면 각 단계가 IN$>5$, CD, F1, ECD, EF1을 일관되게 개선한다.
3. Mesh reconstruction benchmark에서 FlexiCubes는 DMTet/MC보다 ground-truth geometry alignment와 sliver triangle 억제가 좋다.
4. nvdiffrec, GET3D, physics simulation 같은 실제 differentiable pipeline에 넣어도 동작하며, 일부 metric과 qualitative mesh quality가 개선된다.

### 4. Method

#### 4.1 Dual Marching Cubes 기반 extraction

FlexiCubes는 scalar function $s(\mathbf{x})$가 grid vertex에서 갖는 sign으로 DMC connectivity를 정한다. Marching Cubes가 grid edge 위 zero-crossing에서 primal vertex를 만들고 cell 안 face를 구성하는 반면, DMC는 primal face마다 dual vertex를 만들고 adjacent cell의 dual vertex를 연결해 quadrilateral mesh를 만든다. 이 구조는 어려운 configuration에서 cell 하나가 여러 dual vertex를 낼 수 있어 topology를 더 안정적으로 다룰 수 있다.

#### 4.2 Flexible dual vertex positioning

일반 DMC에서 edge crossing은 scalar value의 linear interpolation으로 정해진다. FlexiCubes는 cube corner별 positive interpolation weight $\alpha$를 도입해 zero-crossing 위치를 조정한다. 추출된 dual vertex도 primal face crossing들의 단순 centroid 대신 cube edge별 positive weight $\beta$로 weighted combination한다.

중요한 점은 두 식이 모두 convex combination 형태로 설계되어 dual vertex가 cell의 convex hull 안에 머물게 된다는 것이다. 이 제한은 표현력을 완전히 풀어버리지 않으면서 optimization 중 self-intersection과 degeneracy를 억제하려는 설계다. 논문은 $\tanh(\cdot)+1$ activation으로 weight 범위를 $[0,2]$로 제한한다고 설명한다.

#### 4.3 Flexible quad splitting

DMC/FlexiCubes는 기본적으로 non-planar quadrilateral mesh를 만든다. Downstream rendering이나 processing을 위해 triangle로 split해야 하는데, 임의 diagonal split은 curved region에서 artifact를 만들 수 있다. FlexiCubes는 grid cell별 splitting weight $\gamma$를 두고, optimization 중에는 quad 중심에 midpoint를 추가해 네 triangle로 나누는 differentiable surrogate를 사용한다. Inference에서는 더 큰 $\gamma$ product를 갖는 diagonal을 선택해 두 triangle로 split한다.

#### 4.4 Grid deformation

DefTet와 DMTet처럼 underlying grid vertex에 displacement $\mathbf{d} \in \mathbb{R}^3$를 둔다. 이 deformation은 thin feature나 local alignment를 더 잘 맞추기 위한 추가 자유도다. 단, grid cell inversion을 막기 위해 displacement 크기를 grid spacing의 절반 이하로 제한한다.

#### 4.5 Tetrahedral mesh와 adaptive mesh

FlexiCubes는 surface mesh뿐 아니라 interior tetrahedral mesh도 선택적으로 출력한다. tetrahedralization은 grid vertex, extracted surface vertex, surface vertex가 없는 cell의 midpoint를 vertex set으로 사용하고, grid edge sign 관계에 따라 tetrahedra를 만든다. 이는 differentiable physics simulation과 character animation 같은 응용을 겨냥한다.

Adaptive mesh resolution은 octree refinement로 구현된다. 서로 다른 level의 cell이 만날 때 cracks나 non-manifold surface가 생길 수 있으므로, refined octree vertex의 SDF 값을 coarse face에서 bilinear interpolation한 값으로 묶어 sign consistency를 강제한다. 완전한 guarantee는 아니지만 실험에서는 거의 watertight adaptive mesh를 얻었다고 보고한다.

#### 4.6 Regularizers

FlexiCubes는 over-parameterized representation이므로 두 내부 regularizer를 둔다.

첫째, $L_\mathrm{dev}$는 dual vertex와 관련 edge crossing들 사이 거리의 mean absolute deviation을 줄인다. 이는 extracted connectivity를 안정화하고 vertex가 cell 중앙 근처에서 “움직일 여유”를 갖도록 유도한다.

둘째, $L_\mathrm{sign}$은 supervision이 없는 내부 cavity나 floating geometry를 줄이기 위해 grid edge sign change를 penalize한다. Munkberg et al. 2022의 방식처럼 grid edge 양끝 scalar value의 sign consistency를 cross-entropy 형태로 제어한다.

### 5. 수학적 배경

논문의 기본 formulation은 scalar field의 $0$-isosurface extraction이다. grid edge 양끝의 scalar value가 다른 sign을 가지면 edge crossing $\mathbf{u}$를 만든다. 일반 Marching 방식의 zero-crossing은 다음과 같은 interpolation으로 볼 수 있다.

$$
\mathbf{u}
=
\frac{s(\mathbf{x}_i)\mathbf{x}_j - s(\mathbf{x}_j)\mathbf{x}_i}
{s(\mathbf{x}_i)-s(\mathbf{x}_j)}.
$$

FlexiCubes는 이 interpolation에 positive weight를 넣어 crossing 위치를 local하게 움직인다. 이후 dual vertex $\mathbf{v}$는 face crossing set $U$의 weighted centroid로 계산된다.

$$
\mathbf{v}
=
\frac{\sum_{\mathbf{u}_k \in U} \beta_k \mathbf{u}_k}
{\sum_{\mathbf{u}_k \in U} \beta_k}.
$$

이 형태의 장점은 $\beta_k > 0$이면 $\mathbf{v}$가 crossing들의 convex hull 안에 남는다는 점이다. 즉, DC처럼 QEF가 cell 밖 vertex를 만들 위험을 줄이면서도, centroid-only DMC보다 위치 조정 자유도를 얻는다.

Quad splitting에서는 네 꼭짓점 $\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3,\mathbf{v}_4$를 가진 quad에 대해 두 diagonal 후보의 midpoint를 splitting weight로 interpolation하는 surrogate를 둔다. 정확한 notation은 본문 Figure 8 기준이지만, 핵심은 “두 가능한 triangulation 사이를 continuous하게 interpolate해 gradient가 split preference를 학습하게 한다”는 것이다.

### 6. 실험

#### 6.1 Mesh reconstruction

실험은 Myles et al. 2014의 79개 shape를 사용한다. 각 iteration에서 mesh를 추출하고 random camera pose에서 depth와 silhouette을 렌더링한 뒤, ground truth depth/silhouette과 비교한다. 또한 1000개 random point의 SDF loss를 계산한다. 비교군은 differentiable isosurfacing 계열의 MC, DMTet과, fixed ground-truth SDF에서 post-processing으로 추출하는 MC, DC, NDC다.

주요 metric은 Chamfer Distance (CD), F1, Edge Chamfer Distance (ECD), Edge F1 (EF1), inaccurate normal 비율 IN$>5$, triangle aspect ratio, radius ratio, min/max angle이다.

대표 결과는 다음과 같다.

| 설정 | 방법 | IN$>5$ (%) | CD $(10^{-5})$ | F1 | ECD $(10^{-2})$ | EF1 | 해석 |
|---|---:|---:|---:|---:|---:|---:|---|
| $64^3$ 수준 | DMTet(80) | 48.66 | 5.17 | 0.66 | 3.59 | 0.29 | geometry는 괜찮지만 edge/detail과 triangle quality가 제한적 |
| $64^3$ 수준 | FlexiCubes | 34.87 | 4.87 | 0.70 | 0.71 | 0.43 | normal, Chamfer, edge fidelity 모두 개선 |
| $128^3$ 수준 | DMTet(128) | 48.86 | 4.98 | 0.74 | 1.50 | 0.39 | 고해상도에서도 sliver triangle 문제가 남음 |
| $128^3$ 수준 | FlexiCubes | 30.57 | 4.31 | 0.71 | 0.42 | 0.51 | edge fidelity와 normal consistency가 특히 강함 |

Ablation도 설계 의도를 뒷받침한다. $64^3$에서 Nielson DMC centroid는 IN$>5=53.02$, CD $=5.85$, F1 $=0.65$인데, flexible vertex를 넣으면 IN$>5=40.88$, CD $=5.34$, F1 $=0.68$로 개선된다. Grid deformation을 추가하면 CD $=5.01$, EF1 $=0.41$이 되고, flexible quad split까지 넣은 full FlexiCubes는 IN$>5=34.87$, CD $=4.87$, F1 $=0.70$, ECD $=0.71$, EF1 $=0.43$까지 좋아진다.

#### 6.2 Mesh-based regularization

FlexiCubes는 extracted mesh 자체에 정의되는 regularizer를 automatic differentiation으로 직접 걸 수 있다. 논문은 equilateral edge length regularization과 developability energy를 예시로 든다.

Equilateral regularizer를 추가하면 FlexiCubes의 triangle quality는 크게 개선되고 geometry drop은 작다. Table 4 기준으로 FlexiCubes는 regularizer 전 IN$>5=34.87$, CD $=4.87$, min angle $<10^\circ$ 비율 $2.04\%$였고, regularizer 후 IN$>5=41.05$, CD $=5.46$, min angle $<10^\circ$ 비율 $0.24\%$가 된다. DMTet은 triangle quality는 좋아지지만 IN$>5$가 $48.66$에서 $67.65$로 크게 악화된다.

Developability 실험은 sheet metal이나 plywood처럼 panel fabrication이 필요한 표면을 겨냥한다. FlexiCubes는 shape feature를 보존하면서 developability term을 만족하는 mesh를 찾지만, Marching Cubes는 rigid한 extraction 때문에 feature preservation과 regularizer 만족을 동시에 달성하기 어렵다.

### 7. Applications

#### 7.1 Photogrammetry through differentiable rendering

nvdiffrec의 topology optimization stage에서 DMTet을 FlexiCubes로 교체한다. 나머지 pipeline은 거의 유지한다. NeRF synthetic dataset의 view interpolation PSNR은 대체로 비슷하지만, visible triangle CD는 여러 scene에서 크게 좋아진다. 예를 들어 Chair는 DMTet $4.51$에서 FlexiCubes $0.45$, Hotdog는 $2.67$에서 $1.44$, Lego는 $2.41$에서 $1.60$, Ship은 $55.8$에서 $10.5$로 개선된다. Real-world Family/GoldCape에서도 PSNR은 비슷하고, FlexiCubes가 더 uniform한 tessellation과 더 나은 detail capture를 보인다.

#### 7.2 Animated object mesh simplification

RenderPeople animation에서 known skeleton과 image supervision을 사용해 low-poly mesh를 최적화한다. T-pose만 맞춘 뒤 후처리로 skinning하는 baseline과 달리, FlexiCubes는 each iteration에서 re-skinning과 rendering loss를 같이 통과시켜 animation 전체에 대해 end-to-end 최적화한다. 결과적으로 triangle density가 motion에 맞게 재분배되어 stretching이 줄고, fixed topology template deformation보다 topology까지 최적화할 수 있다.

#### 7.3 3D mesh generation

GET3D의 DMTet extraction module을 FlexiCubes로 교체한다. 변경은 3D generator의 마지막 layer가 cube마다 FlexiCubes weight 21개를 추가 출력하게 하는 정도이며, training procedure, ShapeNet dataset, hyperparameter는 유지한다. FID는 Motorbike $48.90 \rightarrow 44.87$, Chair $22.41 \rightarrow 17.51$, Car $10.60 \rightarrow 9.55$로 개선된다. 정성적으로도 thin structure와 surface uniformity가 더 낫다고 보고한다.

#### 7.4 Differentiable physics simulation

FlexiCubes가 tetrahedral mesh를 differentiably 출력할 수 있다는 점을 이용해 GradSim과 differentiable renderer에 연결한다. Multi-view video에서 rest-pose geometry, texture, mass density 같은 physical parameter를 복원하는 실험이다. 논문 예시에서는 ground-truth mass density $\rho=0.300$에 대해 optimized $\rho=0.311$까지 근접한다.

### 8. 기존 방법과 비교

| 방법 | 장점 | 한계 | FlexiCubes와의 차이 |
|---|---|---|---|
| Marching Cubes / Marching Tetrahedra | 단순하고 differentiable 구현이 쉬우며 intersection-free 성질이 강함 | vertex가 grid edge에 묶여 sharp feature와 non-axis-aligned geometry를 잘 못 맞추고 sliver triangle이 생김 | FlexiCubes는 cell 내부 dual vertex와 grid deformation으로 local alignment 자유도를 늘림 |
| Dual Contouring | sharp feature capture에 강함 | QEF solution이 cell 밖으로 나가거나 coplanar normal에서 singularity가 생겨 optimization이 불안정할 수 있음 | FlexiCubes는 convex weighted combination으로 위치를 제한해 실용적 안정성을 높임 |
| Neural Dual Contouring | fixed field extraction quality가 좋고 sharp feature를 학습적으로 다룸 | optimization 중 pretrained network와 SDF update를 결합하기 어렵고 Figure 4에서 divergence 사례가 있음 | FlexiCubes는 downstream objective에 직접 맞춰 extraction parameter를 같이 최적화 |
| DMTet | differentiable 3D mesh generation의 강한 baseline이며 nvdiffrec/GET3D에 이미 쓰임 | 많은 sliver triangle, local feature alignment 부족, mesh-based regularizer 적용 시 geometry trade-off가 큼 | FlexiCubes는 DMTet을 plug-in 대체하면서 tessellation uniformity와 edge fidelity를 개선 |
| Template mesh deformation | topology가 고정되어 안정적인 경우가 있음 | topology 변화가 어렵고 초기 template에 민감함 | FlexiCubes는 scalar field 기반이라 topology를 optimization 중 바꿀 수 있음 |

### 9. Robotics 관점의 novelty와 relevance

Robotics에서 이 논문의 직접적 의미는 **perception-to-simulation 또는 perception-to-planning에 들어갈 mesh를 differentiable pipeline 안에서 더 좋은 품질로 얻을 수 있다**는 점이다. 로봇 manipulation, scene reconstruction, deformable object modeling, differentiable simulation은 모두 mesh element quality와 watertightness, self-intersection 여부에 민감하다.

특히 tetrahedral mesh extraction은 FEM 기반 deformable object simulation, tactile/visual inverse physics, material parameter estimation에 중요하다. 기존 vision-only 3D reconstruction에서는 “보기에 그럴듯한 surface”가 충분할 수 있지만, robotics deployment에서는 sliver tetrahedra, self-intersection, non-manifold edge가 simulation blow-up이나 contact artifact를 만들 수 있다. FlexiCubes는 이 문제를 완전히 해결하지는 않지만, DMTet보다 더 uniform하고 feature-aligned mesh를 differentiable하게 얻는 방향을 제시한다.

또한 animated object simplification 실험은 robot imitation, human-object interaction dataset, digital twin compression에도 연결된다. 다만 real robot setting에서는 noisy multi-view observation, occlusion, material/contact uncertainty가 훨씬 크므로 본 논문의 evidence를 그대로 deployment robustness로 해석하면 안 된다.

### 10. 한계와 failure case

첫째, FlexiCubes는 self-intersection-free를 보장하지 않는다. Core algorithm은 manifoldness를 보장하도록 설계되지만, flexible dual vertex가 움직이면서 intersecting configuration이 생길 수 있다. 논문은 $64^3$ reconstruction benchmark에서 self-intersecting triangle 비율이 $0.10\%$로 DC variant보다 낮다고 보고하지만, watertight mesh가 필수인 simulation이나 fabrication에서는 추가 검사가 필요하다.

둘째, global continuity나 formal differentiability를 보장하지 않는다. Isosurface가 grid vertex를 지나갈 때 topology가 jump하며, 이는 DC/DMC 계열에서 상속된 성질이다. 저자들은 Adam 기반 stochastic optimization에서는 문제가 크지 않았다고 설명하지만, 이론적 smooth optimization layer로 보기에는 제한이 있다.

셋째, FlexiCubes는 MC/DMTet보다 runtime과 memory가 더 크다. $64^3$에서 FlexiCubes forward/backward는 $8.93/7.32$ ms, memory는 $116.56$ MB로, DMTet의 $2.33/1.38$ ms, $22.44$ MB보다 무겁다. $128^3$에서도 memory가 $816.17$ MB까지 증가한다. Downstream task 전체 비용에 비하면 작을 수 있지만, embedded robotics나 large-scale scene reconstruction에서는 부담이 될 수 있다.

넷째, tetrahedral/adaptive extension은 surface extraction보다 guarantee가 약하다. Ambiguous DMC configuration에서 작은 cavity, non-manifold element, tiny-volume tetrahedra가 생길 수 있고, supplement에서는 volume threshold filtering이 필요하다고 설명한다. 이는 physics simulation에서 stiffness matrix conditioning에 영향을 줄 수 있다.

### 11. 결론

FlexiCubes는 “isosurface extraction은 단순 후처리가 아니라 differentiable optimization의 핵심 representation”이라는 점을 분명히 보여주는 논문이다. DMC topology 위에 interpolation weight, dual vertex weight, quad splitting weight, grid deformation을 넣어, MC/DMTet의 안정성과 DC의 feature flexibility 사이에서 실용적인 균형을 찾는다.

논문의 강점은 method가 추상적 제안에 그치지 않고 nvdiffrec, GET3D, differentiable physics simulation까지 연결된다는 점이다. 반면 guarantee는 완전하지 않고, self-intersection, discontinuity, memory overhead, adaptive/tetrahedral extension의 corner case는 robotics deployment 전에 반드시 별도 validation이 필요하다.

후속 연구로는 volumetric rendering과 mesh representation의 결합, 4D spatiotemporal meshing, adaptive hierarchical representation의 integration, 더 강한 non-intersection 또는 tetrahedral quality regularization이 자연스럽다.

## 추가 질문과 답변
