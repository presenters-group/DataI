import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-taps',
  templateUrl: './taps.component.html',
  styleUrls: ['./taps.component.scss']
})
export class TapsComponent implements OnInit {
  currentTapIndex = 0;
  taps= [
    {
      name: "table 1",
      type: "data-source"
    },{
      name: "filter 1",
      type: "filter"
    },{
      name: "dashboard 1",
      type: "dashboard"
    }
  ]
  constructor(private router : Router) { }

  ngOnInit(): void {
  }
  onClick(i : number) : void{
    this.router.navigate([this.taps[i].type])
    this.currentTapIndex = i
  }
  onClose(i : number) : void{
    this.taps = this.taps.filter((tap,index) => index != i)
     this.currentTapIndex = i != 0 ? i - 1 : 0;
  }
}




// const cos = Math.cos;
// const sin = Math.sin;
// const π = Math.PI;

// const f_matrix_times = (( [[a,b], [c,d]], [x,y]) => [ a * x + b * y, c * x + d * y]);
// const f_rotate_matrix = ((x) => [[cos(x),-sin(x)], [sin(x), cos(x)]]);
// const f_vec_add = (([a1 , a2], [b1, b2]) => [a1 + b1, a2 + b2]);

// const f_svg_ellipse_arc = (([cx,cy ],[rx,ry], [t1, Δ], φ ) => {
// /* [
// returns a SVG path element that represent a ellipse.
// cx,cy → center of ellipse
// rx,ry → major minor radius
// t1 → start angle, in radian.
// Δ → angle to sweep, in radian. positive.
// φ → rotation on the whole, in radian
// URL: SVG Circle Arc http://xahlee.info/js/svg_circle_arc.html
// Version 2019-06-19
//  ] */
// Δ = Δ % (2*π);
// const rotMatrix = f_rotate_matrix (φ);
// const [sX, sY] = ( f_vec_add ( f_matrix_times ( rotMatrix, [rx * cos(t1), ry * sin(t1)] ), [cx,cy] ) );
// const [eX, eY] = ( f_vec_add ( f_matrix_times ( rotMatrix, [rx * cos(t1+Δ), ry * sin(t1+Δ)] ), [cx,cy] ) );
// const fA = ( (  Δ > π ) ? 1 : 0 );
// const fS = ( (  Δ > 0 ) ? 1 : 0 );
// const path_2wk2r = document.createElementNS("http://www.w3.org/2000/svg", "path");
// path_2wk2r.setAttribute("d", "M " + sX + " " + sY + " A " + [ rx , ry , φ / (2*π) *360, fA, fS, eX, eY ].join(" "));
// return path_2wk2r;
// });
