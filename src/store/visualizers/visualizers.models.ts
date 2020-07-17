export interface IVisualizer {
  id: number;
  data: number;
  usedColumns: number[];
  xColumn: number;
  chart: string;
  name: string;
  filters: any[];
  isDeleted: boolean;
  chartSvg?: string;
}
